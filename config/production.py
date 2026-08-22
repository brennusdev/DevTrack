"""
Configurações específicas do ambiente
de produção.
"""


from config.base import BaseConfig


class ProductionConfig(BaseConfig):
    """
    Configuração utilizada em produção.
    """

    DEBUG = False