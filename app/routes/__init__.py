"""
Pacote principal da aplicação DevTrack.

Este módulo cria a aplicação Flask através
do Application Factory Pattern.
"""

from flask import Flask

from app.config import Config


def create_app():
    """
    Cria e configura uma instância da aplicação Flask.

    Returns:
        Flask: aplicação Flask configurada.
    """

    # Criamos a aplicação Flask.
    app = Flask(__name__)

    # Carregamos as configurações centralizadas.
    app.config.from_object(Config)

    # --------------------------------------------------
    # BLUEPRINT DA PÁGINA INICIAL
    # --------------------------------------------------

    # Importamos o Blueprint da página inicial.
    from app.routes.home import home_bp

    # Registramos o Blueprint na aplicação.
    app.register_blueprint(home_bp)

    # --------------------------------------------------
    # BLUEPRINT DO DASHBOARD
    # --------------------------------------------------

    # Importamos o Blueprint do Dashboard.
    from app.routes.dashboard import dashboard_bp

    # Registramos o Blueprint.
    #
    # Como dashboard_bp possui o prefixo:
    #
    # /dashboard
    #
    # a rota definida como "/" dentro dele será acessada
    # através de:
    #
    # /dashboard/
    app.register_blueprint(dashboard_bp)

    # Retornamos a aplicação configurada.
    return app