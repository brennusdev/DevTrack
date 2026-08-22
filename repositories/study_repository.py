"""
Repository responsável pelas operações
de banco relacionadas aos estudos.
"""


from models import Study


class StudyRepository:
    """
    Centraliza operações de persistência dos estudos.
    """

    @staticmethod
    def get_by_id(study_id):
        """
        Busca um estudo pelo ID.
        """

        return Study.query.get(
            study_id
        )


    @staticmethod
    def get_by_user(user_id):
        """
        Retorna todos os estudos de um usuário.
        """

        return (
            Study.query
            .filter_by(
                user_id=user_id
            )
            .order_by(
                Study.id.desc()
            )
            .all()
        )


    @staticmethod
    def count_by_user(user_id):
        """
        Conta as sessões de estudo
        de determinado usuário.
        """

        return (
            Study.query
            .filter_by(
                user_id=user_id
            )
            .count()
        )