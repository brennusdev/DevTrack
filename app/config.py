"""
Configurações centrais do DevTrack.

Este módulo concentra as configurações utilizadas
pela aplicação.

A partir da V3 também teremos as configurações
relacionadas ao banco de dados.
"""

import os


class Config:
    """
    Configuração padrão da aplicação.
    """

    # --------------------------------------------------
    # FLASK
    # --------------------------------------------------

    # Chave utilizada pelo Flask para recursos que
    # dependem de assinatura e segurança.
    #
    # Nesta etapa ainda utilizamos um valor de
    # desenvolvimento.
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "devtrack-development-key",
    )

    # Ativa o modo de desenvolvimento.
    DEBUG = True


    # --------------------------------------------------
    # DATABASE
    # --------------------------------------------------

    # Define onde o banco SQLite será armazenado.
    #
    # SQLite é um banco de dados relacional que funciona
    # através de um arquivo.
    #
    # Para a V3 ele é excelente porque não precisamos
    # instalar ou configurar um servidor de banco.
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///devtrack.db",
    )

    # Desativa o sistema antigo de rastreamento de
    # modificações do Flask-SQLAlchemy.
    #
    # Isso reduz consumo desnecessário de memória.
    SQLALCHEMY_TRACK_MODIFICATIONS = False