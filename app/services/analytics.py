"""
Serviço de analytics do DevTrack.
"""
from sqlalchemy import func

from database.db import db

from models import (
    Project,
    Goal,
)


def get_project_progress():
    """
    Retorna os projetos com seus respectivos
    níveis de progresso.

    Returns:
        list:
            Lista contendo nome e progresso
            de cada projeto.
    """

    # Buscamos os projetos ordenados pelo progresso.
    projects = (
        Project.query
        .order_by(
            Project.progress.desc()
        )
        .all()
    )


    # Criamos uma lista vazia.
    result = []


    # Percorremos cada projeto.
    for project in projects:

        # Adicionamos somente os dados necessários
        # para o dashboard.
        result.append(
            {
                "name": project.name,
                "progress": project.progress,
            }
        )


    return result
def get_study_metrics():
    """
    Calcula métricas relacionadas aos estudos.

    Returns:
        dict:
            Métricas de estudo.
    """

    # --------------------------------------------------
    # TOTAL DE SESSÕES
    # --------------------------------------------------

    total_studies = (
        db.session.query(
            func.count(Study.id)
        ).scalar()
    )


    # --------------------------------------------------
    # TOTAL DE HORAS
    # --------------------------------------------------

    total_hours = (
        db.session.query(
            func.sum(Study.hours)
        ).scalar()
    )


    # Se não houver estudos cadastrados,
    # SUM pode retornar None.
    total_hours = (
        float(total_hours)
        if total_hours is not None
        else 0
    )


    # --------------------------------------------------
    # MÉDIA DE HORAS
    # --------------------------------------------------

    average_hours = (
        db.session.query(
            func.avg(Study.hours)
        ).scalar()
    )


    average_hours = (
        float(average_hours)
        if average_hours is not None
        else 0
    )


    return {
        "total_sessions": total_studies or 0,
        "total_hours": round(
            total_hours,
            1,
        ),
        "average_hours": round(
            average_hours,
            1,
        ),
    }
def get_goal_metrics():
    """
    Calcula métricas relacionadas às metas.

    Returns:
        dict:
            Métricas das metas.
    """

    # Total de metas.
    total_goals = (
        db.session.query(
            func.count(Goal.id)
        ).scalar()
    )


    # Metas concluídas.
    completed_goals = (
        db.session.query(
            func.count(Goal.id)
        )
        .filter(
            Goal.completed.is_(True)
        )
        .scalar()
    )


    # Progresso médio.
    average_progress = (
        db.session.query(
            func.avg(Goal.progress)
        ).scalar()
    )


    average_progress = (
        float(average_progress)
        if average_progress is not None
        else 0
    )


    return {
        "total": total_goals or 0,

        "completed": (
            completed_goals or 0
        ),

        "pending": (
            (total_goals or 0)
            -
            (completed_goals or 0)
        ),

        "average_progress": round(
            average_progress,
            1,
        ),
    }