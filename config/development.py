"""
Configurações específicas do ambiente
de desenvolvimento.
"""


from config.base import BaseConfig


class DevelopmentConfig(BaseConfig):
    """
    Configuração utilizada durante o desenvolvimento.
    """

    DEBUG = True