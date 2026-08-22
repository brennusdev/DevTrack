"""
Repository responsável pelas operações
de banco relacionadas às metas.
"""


from models import Goal


class GoalRepository:
    """
    Centraliza consultas e operações
    relacionadas às metas.
    """

    @staticmethod
    def get_by_id(goal_id):
        """
        Busca uma meta pelo ID.
        """

        return Goal.query.get(
            goal_id
        )


    @staticmethod
    def get_by_user(user_id):
        """
        Retorna todas as metas de um usuário.
        """

        return (
            Goal.query
            .filter_by(
                user_id=user_id
            )
            .order_by(
                Goal.id.desc()
            )
            .all()
        )


    @staticmethod
    def count_by_user(user_id):
        """
        Conta quantas metas pertencem
        a determinado usuário.
        """

        return (
            Goal.query
            .filter_by(
                user_id=user_id
            )
            .count()
        )