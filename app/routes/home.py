"""
Rotas relacionadas à página inicial do DevTrack.
"""

from flask import Blueprint, render_template


# Criamos um Blueprint para organizar as rotas
# relacionadas à página inicial.
#
# Um Blueprint permite dividir uma aplicação Flask
# grande em módulos menores e independentes.
home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():
    """
    Exibe a página inicial do DevTrack.

    Returns:
        HTML renderizado a partir do template home.html.
    """

    # render_template procura o arquivo HTML
    # dentro da pasta templates da aplicação.
    return render_template("home.html")