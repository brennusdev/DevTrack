"""
Configuração da extensão SQLAlchemy.

Este módulo cria o objeto responsável por conectar
a aplicação Flask à camada ORM do SQLAlchemy.
"""

from flask_sqlalchemy import SQLAlchemy


# Criamos a instância da extensão.

# Importante:
#
# Ainda não associamos essa instância a uma aplicação
# Flask específica.
#
# Isso será feito durante a inicialização da aplicação.
db = SQLAlchemy()