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