"""
Repository responsável pelas operações
de banco relacionadas aos projetos.
"""


from models import Project


class ProjectRepository:
    """
    Centraliza consultas relacionadas aos projetos.
    """

    @staticmethod
    def get_by_id(project_id):
        """
        Busca um projeto pelo ID.

        Args:
            project_id: identificador do projeto.

        Returns:
            Projeto encontrado ou None.
        """

        return Project.query.get(
            project_id
        )


    @staticmethod
    def get_by_user(user_id):
        """
        Retorna todos os projetos pertencentes
        a determinado usuário.

        Args:
            user_id: identificador do usuário.

        Returns:
            Lista de projetos.
        """

        return (
            Project.query
            .filter_by(
                user_id=user_id
            )
            .order_by(
                Project.id.desc()
            )
            .all()
        )


    @staticmethod
    def count_by_user(user_id):
        """
        Conta quantos projetos um usuário possui.
        """

        return (
            Project.query
            .filter_by(
                user_id=user_id
            )
            .count()
        )