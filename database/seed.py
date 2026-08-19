"""
Seed inicial do banco de dados.

Seed significa inserir dados iniciais para que
a aplicação tenha informações disponíveis durante
o desenvolvimento.

Este arquivo não representa os dados definitivos
do sistema.
"""

from app import create_app

from database.db import db

from app.models import (
    Project,
    Study,
    Goal,
    Activity,
)


# Criamos a aplicação Flask.
app = create_app()


def seed_database():
    """
    Insere dados iniciais no banco.
    """

    # Criamos um contexto da aplicação porque
    # precisamos acessar recursos relacionados ao Flask
    # e ao banco de dados.
    with app.app_context():

        # --------------------------------------------------
        # PROJETOS
        # --------------------------------------------------

        project_1 = Project(
            name="DevTrack",
            technology="Python",
            progress=32,
        )


        project_2 = Project(
            name="Nexus Core",
            technology="Python / Web",
            progress=68,
        )


        project_3 = Project(
            name="Méd",
            technology="Python",
            progress=41,
        )


        # --------------------------------------------------
        # ESTUDOS
        # --------------------------------------------------

        study_1 = Study(
            technology="Python",
            hours=3.5,
            description="Arquitetura de aplicações Flask",
        )


        study_2 = Study(
            technology="SQL",
            hours=2.0,
            description="Introdução a banco de dados relacionais",
        )


        study_3 = Study(
            technology="Docker",
            hours=1.5,
            description="Conceitos básicos de containers",
        )


        # --------------------------------------------------
        # METAS
        # --------------------------------------------------

        goal_1 = Goal(
            title="Finalizar DevTrack V1",
            progress=100,
            completed=True,
        )


        goal_2 = Goal(
            title="Aprender SQL",
            progress=40,
            completed=False,
        )


        # --------------------------------------------------
        # ATIVIDADES
        # --------------------------------------------------

        activity_1 = Activity(
            type="commit",
            title="Commit realizado",
            description="Evolução do projeto DevTrack",
        )


        activity_2 = Activity(
            type="study",
            title="Estudo concluído",
            description="Estudo de Python",
        )


        activity_3 = Activity(
            type="goal",
            title="Meta atualizada",
            description="Progresso da meta de SQL",
        )


        # --------------------------------------------------
        # ADICIONANDO AO BANCO
        # --------------------------------------------------

        # add_all permite adicionar vários objetos
        # à sessão de uma única vez.
        db.session.add_all(
            [
                project_1,
                project_2,
                project_3,
                study_1,
                study_2,
                study_3,
                goal_1,
                goal_2,
                activity_1,
                activity_2,
                activity_3,
            ]
        )


        # commit confirma definitivamente as alterações.
        db.session.commit()


        print("Banco populado com sucesso.")


if __name__ == "__main__":

    seed_database()