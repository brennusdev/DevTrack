"""
Rotas relacionadas ao Dashboard.
"""

from flask import Blueprint, render_template

from app.database.db import db

from app.models import (
    Project,
    Study,
    Goal,
    Activity,
)


dashboard_bp = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/dashboard",
)


@dashboard_bp.route("/")
def dashboard():
    """
    Exibe o Dashboard utilizando dados do banco.

    Returns:
        HTML renderizado com dados persistidos.
    """

    # --------------------------------------------------
    # PROJETOS
    # --------------------------------------------------

    # Busca todos os projetos cadastrados.
    projects = Project.query.all()


    # --------------------------------------------------
    # ESTUDOS
    # --------------------------------------------------

    # Busca todos os registros de estudo.
    studies = Study.query.all()


    # Calculamos o total de horas estudadas.
    #
    # sum() percorre os registros e soma o valor
    # armazenado em "hours".
    study_hours = sum(
        study.hours
        for study in studies
    )


    # --------------------------------------------------
    # METAS
    # --------------------------------------------------

    # Busca todas as metas.
    goals = Goal.query.all()


    # Conta quantas metas foram concluídas.
    completed_goals = sum(
        1
        for goal in goals
        if goal.completed
    )


    # --------------------------------------------------
    # ATIVIDADES
    # --------------------------------------------------

    # Busca todas as atividades.
    #
    # order_by() organiza os registros pela data
    # mais recente primeiro.
    activities = (
        Activity.query
        .order_by(Activity.created_at.desc())
        .all()
    )


    # --------------------------------------------------
    # MÉTRICAS
    # --------------------------------------------------

    metrics = {
        "study_hours": study_hours,
        "projects": len(projects),
        "completed_goals": completed_goals,
        "current_streak": 12,
    }


    # --------------------------------------------------
    # TECNOLOGIAS
    # --------------------------------------------------

    # Por enquanto mantemos as tecnologias como uma
    # lista simples.
    #
    # Posteriormente criaremos uma entidade própria
    # para tecnologias.
    technologies = [
        "Python",
        "SQL",
        "Flask",
        "HTML",
        "CSS",
        "Docker",
    ]


    # --------------------------------------------------
    # TEMPLATE
    # --------------------------------------------------

    return render_template(
        "dashboard.html",
        metrics=metrics,
        projects=projects,
        technologies=technologies,
        activities=activities,
    )