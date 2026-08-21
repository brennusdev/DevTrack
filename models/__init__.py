"""
Centraliza a importação dos modelos do DevTrack.

Importar os modelos neste arquivo facilita garantir
que o SQLAlchemy conheça todas as tabelas antes
da criação do banco.
"""
from models.user import User  

from models.project import Project
from models.study import Study
from models.goal import Goal
from models.activity import Activity


__all__ = [
    "Project",
    "Study",
    "Goal",
    "Activity",
]