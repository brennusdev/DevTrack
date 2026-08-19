"""
Pacote principal da aplicação DevTrack.

Este módulo é responsável por criar e configurar
a aplicação Flask através do Application Factory Pattern.

O uso de uma factory facilita futuramente:

- criação de diferentes ambientes;
- testes automatizados;
- configuração de desenvolvimento;
- configuração de produção;
- inicialização controlada da aplicação.
"""

from flask import Flask
from app.routes.projects import projects_bp
from app.routes.home import home_bp
from app.routes.dashoboard import dashboard_bp
from app.routes.projects import projects_bp
from app.config import Config
from app.routes.studies import studies_bp
from app.routes.goals import goals_bp






def create_app():
    """
    Cria uma nova instância da aplicação Flask.

    Returns:
        Flask: aplicação Flask configurada.
    """

    # Criamos a instância principal do Flask.
    #
    # __name__ informa ao Flask qual é o módulo atual.
    # Isso permite que o framework consiga localizar
    # recursos como templates e arquivos estáticos.
    app = Flask(__name__)

    # Carregamos as configurações definidas na classe Config.
    #
    # Dessa maneira evitamos colocar configurações
    # diretamente espalhadas pelo código da aplicação.
    app.config.from_object(Config)

    # Importamos as rotas dentro da função.
    #
    # Fazer o import aqui ajuda a evitar problemas
    # de importação circular durante a inicialização.
    from app.routes.home import home_bp

    # Registramos o Blueprint responsável pelas
    # rotas da página inicial.
    app.register_blueprint(home_bp)

    # Retornamos a aplicação pronta para ser executada.
    return app

from models import (
    Project,
    Study,
    Goal,
    Activity,
)