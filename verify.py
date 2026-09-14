"""
=====================================================
DEVTRACK - SCRIPT DE VERIFICAÇÃO DO PROJETO
=====================================================

Este script verifica se o projeto está íntegro e
rodando corretamente.

Etapas executadas:

1. Compilação de todos os arquivos .py (erros de sintaxe);
2. Import da Application Factory sem erros;
3. Verificação de rotas duplicadas (endpoint x função);
4. Verificação de variáveis obrigatórias de configuração;
5. Smoke test: cada rota GET responde com status válido;
6. Verificação de templates órfãos
   (render_template apontando para arquivo inexistente).

Como executar:

    python verify.py

Código de saída 0 = projeto saudável.
Código de saída 1 = encontrou problemas.
"""

import os
import sys
import py_compile
from pathlib import Path

# Garante que rodamos a partir da raiz do projeto.
os.chdir(Path(__file__).parent)
sys.path.insert(0, str(Path(__file__).parent))

# Garante que SECRET_KEY exista (o .env é carregado
# pela própria aplicação, mas este script roda fora dela).
os.environ.setdefault("SECRET_KEY", "verify-script-key")

# Lista para acumular os problemas encontrados.
problems = []


def check(title, func):
    """
    Executa uma verificação e imprime o resultado.

    Args:
        title: nome amigável da verificação.
        func: função que executa o teste.
              Deve retornar (ok, detalhe).
    """
    try:
        ok, detail = func()
    except Exception as exc:  # noqa: BLE001
        ok, detail = False, f"exceção: {exc}"

    status = "OK  " if ok else "FALHOU"
    print(f"[{status}] {title}")

    if detail:
        print(f"          -> {detail}")

    if not ok:
        problems.append(title)


# =====================================================
# 1. SINTAXE
# =====================================================

def check_syntax():
    """
    Compila todos os arquivos .py do projeto.
    """
    errors = []

    for py_file in Path(".").rglob("*.py"):

        # Ignora caches e ambientes virtuais.
        if "__pycache__" in str(py_file) or ".venv" in str(py_file):
            continue

        try:
            py_compile.compile(str(py_file), doraise=True)
        except py_compile.PyCompileError as exc:
            errors.append(f"{py_file}: {exc}")

    return (len(errors) == 0), "; ".join(errors) or "todos os arquivos compilam"


# =====================================================
# 2. APPLICATION FACTORY
# =====================================================

def check_factory():
    """
    Importa a factory e cria a aplicação.
    """
    from run import app  # noqa: PLC0415

    return True, f"create_app() OK - {len(list(app.url_map.iter_rules()))} rotas"


# =====================================================
# 3. ROTAS
# =====================================================

def check_routes():
    """
    Verifica rotas duplicadas.
    """
    from run import app  # noqa: PLC0415

    seen = {}
    duplicates = []

    for rule in app.url_map.iter_rules():
        key = str(rule)
        if key in seen:
            duplicates.append(key)
        seen[key] = rule.endpoint

    return (len(duplicates) == 0), f"duplicadas: {duplicates}" if duplicates else "sem duplicatas"


# =====================================================
# 4. CONFIGURAÇÃO
# =====================================================

def check_config():
    """
    Verifica se as configurações essenciais existem.
    """
    from run import app  # noqa: PLC0415

    missing = []

    for key in ("SECRET_KEY", "SQLALCHEMY_DATABASE_URI"):
        if not app.config.get(key):
            missing.append(key)

    return (len(missing) == 0), f"ausentes: {missing}" if missing else "configuração completa"


# =====================================================
# 5. SMOKE TEST
# =====================================================

def check_smoke():
    """
    Faz uma requisição GET em cada rota acessível
    sem parâmetros e valida o status HTTP.
    """
    from run import app  # noqa: PLC0415

    client = app.test_client()
    failures = []

    for rule in app.url_map.iter_rules():
        url = str(rule)

        # Pula rotas com parâmetros, static e OPTIONS/HEAD only.
        if "<" in url or url == "/static/<path:filename>":
            continue

        # Só testamos métodos que aceitam GET.
        if "GET" not in rule.methods:
            continue

        response = client.get(url)

        # 200 = OK, 3xx = redirect (aceitável), 500 = erro.
        if response.status_code >= 500:
            failures.append(f"{url} -> {response.status_code}")

    return (len(failures) == 0), f"falhas: {failures}" if failures else "todas as rotas respondem"


# =====================================================
# 6. TEMPLATES
# =====================================================

def check_templates():
    """
    Confere se todos os render_template() apontam
    para arquivos que realmente existem.
    """
    import re  # noqa: PLC0415
    from run import app  # noqa: PLC0415

    # Coleta os nomes usados em render_template("...").
    pattern = re.compile(
        r"render_template\(\s*['\"]([^'\"]+)['\"]"
    )

    used = set()

    for py_file in Path("app").rglob("*.py"):
        content = py_file.read_text(encoding="utf-8", errors="ignore")
        used.update(pattern.findall(content))

    missing = []

    for template in used:
        if not (Path("app/templates") / template).exists():
            missing.append(template)

    return (len(missing) == 0), f"ausentes: {missing}" if missing else f"{len(used)} templates OK"


# =====================================================
# EXECUÇÃO
# =====================================================

CHECKS = [
    ("Sintaxe de todos os arquivos .py", check_syntax),
    ("Application Factory (create_app)", check_factory),
    ("Rotas duplicadas", check_routes),
    ("Configurações essenciais", check_config),
    ("Smoke test das rotas GET", check_smoke),
    ("Templates referenciados existem", check_templates),
]


def main():
    print("=" * 55)
    print("DEVTRACK - VERIFICAÇÃO DO PROJETO")
    print("=" * 55)

    for title, func in CHECKS:
        check(title, func)

    print("=" * 55)

    if problems:
        print(f"RESULTADO: {len(problems)} problema(s) encontrado(s):")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)

    print("RESULTADO: Tudo OK! Projeto íntegro e rodando.")
    sys.exit(0)


if __name__ == "__main__":
    main()
