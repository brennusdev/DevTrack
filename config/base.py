"""
Configurações compartilhadas entre os ambientes
da aplicação.

Este arquivo contém somente configurações
que podem ser utilizadas por diferentes ambientes.
"""


import os


class BaseConfig:
    """
    Configuração base do DevTrack.
    """

    # --------------------------------------------------
    # SECRET KEY
    # --------------------------------------------------

    # A SECRET_KEY é utilizada pelo Flask para
    # proteger sessões e outros mecanismos internos.
    #
    # IMPORTANTE:
    # Em produção, esse valor deve vir de uma
    # variável de ambiente.
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "devtrack-development-key",
    )


    # --------------------------------------------------
    # DATABASE
    # --------------------------------------------------

    # URL utilizada para conexão com o banco.
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///devtrack.db",
    )


    # --------------------------------------------------
    # SQLALCHEMY
    # --------------------------------------------------

    SQLALCHEMY_TRACK_MODIFICATIONS = False