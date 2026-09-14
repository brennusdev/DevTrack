"""
Pacote principal da aplicação DevTrack.

Este módulo é responsável por criar e configurar
a aplicação Flask através do Application Factory Pattern.
"""

from flask import Flask

from app.config import Config

from database.db import db

from models import (
    Project,
    Study,
    Goal,
    Activity,
    User,
)


def create_app():
    """
    Cria uma nova instância da aplicação Flask.

    Returns:
        Flask: aplicação Flask configurada.
    """
    # Criamos a instância principal do Flask.
    app = Flask(__name__)

    # Carregamos as configurações centralizadas.
    app.config.from_object(Config)

    # --------------------------------------------------
    # BANCO DE DADOS
    # --------------------------------------------------
    # Associamos a instância do SQLAlchemy a esta app.
    db.init_app(app)

    # --------------------------------------------------
    # BLUEPRINTS
    # --------------------------------------------------
    # Imports dentro da função evitam importação circular.
    from app.routes.home import home_bp
    from app.routes.dashoboard import dashboard_bp
    from app.routes.projects import projects_bp
    from app.routes.goals import goals_bp
    from app.routes.analytics import analytics_bp
    from app.routes.health import health_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(goals_bp)
    app.register_blueprint(analytics_bp)
    app.register_blueprint(health_bp)

    # --------------------------------------------------
    # ERROR HANDLERS
    # --------------------------------------------------
    from errors.handlers import register_error_handlers

    register_error_handlers(app)

    # --------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # --------------------------------------------------
    with app.app_context():
        db.create_all()

    return app
