"""
Testes do repository de projetos.
"""


from models import User, Project
from repositories.project_repository import (
    ProjectRepository,
)


def test_get_projects_by_user(app):
    """
    Verifica se o repository retorna
    somente os projetos do usuário correto.
    """

    from database.db import db


    with app.app_context():

        # ----------------------------------------------
        # USUÁRIO
        # ----------------------------------------------

        user = User(
            name="Developer",
            email="developer@example.com",
        )

        user.set_password(
            "12345678"
        )


        db.session.add(
            user
        )

        db.session.commit()


        # ----------------------------------------------
        # PROJETO
        # ----------------------------------------------

        project = Project(
            name="DevTrack",
            technology="Python",
            progress=50,
            user_id=user.id,
        )


        db.session.add(
            project
        )

        db.session.commit()


        # ----------------------------------------------
        # CONSULTA
        # ----------------------------------------------

        projects = (
            ProjectRepository
            .get_by_user(
                user.id
            )
        )


        assert len(
            projects
        ) == 1


        assert projects[0].name == "DevTrack"