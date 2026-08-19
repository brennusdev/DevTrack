"""
Rotas responsáveis pelo gerenciamento de projetos.

Este módulo implementa as operações principais
do CRUD de projetos:

CREATE  -> criar
READ    -> consultar/listar
UPDATE  -> atualizar
DELETE  -> excluir
"""

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from database.db import db
from models import Project


# Criamos um Blueprint exclusivo para projetos.
#
# Todas as rotas deste arquivo começarão com:
#
# /projects
#
projects_bp = Blueprint(
    "projects",
    __name__,
    url_prefix="/projects",
)


@projects_bp.route("/")
def list_projects():
    """
    Lista todos os projetos cadastrados.

    Returns:
        HTML contendo os projetos existentes.
    """

    # Busca todos os projetos no banco.
    #
    # .all() retorna uma lista de objetos Project.
    projects = Project.query.all()

    # Enviamos os projetos para o template.
    return render_template(
        "projects/list.html",
        projects=projects,
    )
    @projects_bp.route("/create", methods=["GET", "POST"])
def create_project():
    """
    Cria um novo projeto.

    GET:
        Exibe o formulário.

    POST:
        Processa os dados enviados pelo formulário.
    """

    # Verificamos se o navegador enviou um formulário.
    if request.method == "POST":

        # Recuperamos o nome enviado pelo usuário.
        name = request.form.get("name", "").strip()

        # Recuperamos a tecnologia.
        technology = request.form.get(
            "technology",
            "",
        ).strip()

        # Recuperamos o progresso.
        progress_value = request.form.get(
            "progress",
            "0",
        ).strip()


        # --------------------------------------------------
        # VALIDAÇÃO
        # --------------------------------------------------

        # O nome é obrigatório.
        if not name:

            flash(
                "O nome do projeto é obrigatório.",
                "error",
            )

            return render_template(
                "projects/form.html",
                project=None,
            )


        # A tecnologia também é obrigatória.
        if not technology:

            flash(
                "A tecnologia é obrigatória.",
                "error",
            )

            return render_template(
                "projects/form.html",
                project=None,
            )


        # Tentamos converter o progresso para inteiro.
        try:

            progress = int(progress_value)

        except ValueError:

            flash(
                "O progresso precisa ser um número inteiro.",
                "error",
            )

            return render_template(
                "projects/form.html",
                project=None,
            )


        # O progresso precisa estar entre 0 e 100.
        if progress < 0 or progress > 100:

            flash(
                "O progresso deve estar entre 0 e 100.",
                "error",
            )

            return render_template(
                "projects/form.html",
                project=None,
            )


        # --------------------------------------------------
        # CRIAÇÃO DO OBJETO
        # --------------------------------------------------

        project = Project(
            name = nome,
            technology = tecnologia,
            progress = progresso,
        )


        # Adicionamos o objeto à sessão do SQLAlchemy.
        db.session.add(project)


        # Confirmamos a transação.
        db.session.commit()


        # Mostramos uma mensagem de sucesso.
        flash(
            "Projeto criado com sucesso!",
            "success",
        )


        # Redirecionamos o usuário para a lista.
        return redirect(
            url_for("projects.list_projects")
        )


    # Se for GET, apenas exibimos o formulário.
    return render_template(
        "projects/form.html",
        project=None,
    )
    @projects_bp.route(
    "/<int:project_id>/edit",
    methods=["GET", "POST"],
)
def edit_project(project_id):
    """
    Edita um projeto existente.

    Args:
        project_id: identificador do projeto.

    Returns:
        Página de edição ou redirecionamento.
    """

    # Busca o projeto pelo ID.
    #
    # get_or_404() automaticamente retorna uma página
    # HTTP 404 caso o projeto não exista.
    project = db.get_or_404(
        Project,
        project_id,
    )


    if request.method == "POST":

        name = request.form.get(
            "name",
            "",
        ).strip()

        technology = request.form.get(
            "technology",
            "",
        ).strip()

        progress_value = request.form.get(
            "progress",
            "0",
        ).strip()


        # Validação do nome.
        if not name:

            flash(
                "O nome do projeto é obrigatório.",
                "error",
            )

            return render_template(
                "projects/form.html",
                project=project,
            )


        # Validação da tecnologia.
        if not technology:

            flash(
                "A tecnologia é obrigatória.",
                "error",
            )

            return render_template(
                "projects/form.html",
                project=project,
            )


        # Conversão do progresso.
        try:

            progress = int(progress_value)

        except ValueError:

            flash(
                "O progresso precisa ser um número inteiro.",
                "error",
            )

            return render_template(
                "projects/form.html",
                project=project,
            )


        # Validação do intervalo.
        if progress < 0 or progress > 100:

            flash(
                "O progresso deve estar entre 0 e 100.",
                "error",
            )

            return render_template(
                "projects/form.html",
                project=project,
            )


        # Atualizamos os atributos do objeto.
        project.name = name

        project.technology = technology

        project.progress = progress


        # Confirmamos a alteração.
        db.session.commit()


        flash(
            "Projeto atualizado com sucesso!",
            "success",
        )


        return redirect(
            url_for("projects.list_projects")
        )


    return render_template(
        "projects/form.html",
        project=project,
    )


@projects_bp.route(
    "/<int:project_id>/delete",
    methods=["POST"],
)
def delete_project(project_id):
    """
    Exclui um projeto.

    Args:
        project_id: ID do projeto que será excluído.

    Returns:
        Redirecionamento para a lista de projetos.
    """

    # Localizamos o projeto.
    project = db.get_or_404(
        Project,
        project_id,
    )


    # Removemos o objeto da sessão.
    db.session.delete(project)


    # Confirmamos a exclusão.
    db.session.commit()


    flash(
        "Projeto excluído com sucesso!",
        "success",
    )


    return redirect(
        url_for("projects.list_projects")
    )