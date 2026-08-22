"""
Fixtures compartilhadas pelos testes do DevTrack.

Fixtures são recursos reutilizáveis que podem ser
solicitados pelos testes automaticamente através
dos argumentos das funções de teste.
"""


import pytest


from app import create_app
from database.db import db


@pytest.fixture
def app():
    """
    Cria uma instância da aplicação exclusivamente
    para os testes.
    """

    # --------------------------------------------------
    # CONFIGURAÇÃO DE TESTE
    # --------------------------------------------------

    app = create_app(
        "testing"
    )


    # Ativamos o contexto da aplicação.
    with app.app_context():

        # Criamos as tabelas necessárias
        # para o ambiente de teste.
        db.create_all()


        yield app


        # Depois do teste, removemos
        # as tabelas temporárias.
        db.drop_all()


@pytest.fixture
def client(app):
    """
    Cria um cliente HTTP para testar
    as rotas da aplicação.
    """

    return app.test_client()


def create_app(config_name="development"):
    """
    Cria e configura uma instância Flask.
    """

    app = flask(
        __name__
    )

    # Aqui você poderá selecionar
    # posteriormente a configuração
    # correspondente ao ambiente.

    return app