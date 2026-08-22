"""
Testes relacionados à proteção
das rotas privadas.
"""


def test_dashboard_requires_login(client):
    """
    Usuários não autenticados não devem
    acessar o dashboard.
    """

    response = client.get(
        "/dashboard/"
    )


    # O sistema deve redirecionar
    # para a página de login.
    assert response.status_code == 302
    
def test_projects_require_login(client):
    """
    Verifica se projetos exigem autenticação.
    """

    response = client.get(
        "/projects/"
    )


    assert response.status_code == 302    