"""
Rotas responsáveis pelo módulo de analytics.
"""


from flask import (
    Blueprint,
    render_template,
)


from app.services.analytics import (
    get_project_metrics,
    get_project_progress,
    get_study_metrics,
    get_goal_metrics,
    get_productivity_summary,
)


analytics_bp = Blueprint(
    "analytics",
    __name__,
    url_prefix="/analytics",
)


@analytics_bp.route("/")
def dashboard():
    """
    Exibe o dashboard de analytics.
    """

    # --------------------------------------------------
    # BUSCA DAS MÉTRICAS
    # --------------------------------------------------

    project_metrics = (
        get_project_metrics()
    )


    study_metrics = (
        get_study_metrics()
    )


    goal_metrics = (
        get_goal_metrics()
    )


    productivity = (
        get_productivity_summary()
    )


    project_progress = (
        get_project_progress()
    )


    # --------------------------------------------------
    # RENDERIZAÇÃO
    # --------------------------------------------------

    return render_template(
        "analytics/dashboard.html",

        project_metrics=project_metrics,

        study_metrics=study_metrics,

        goal_metrics=goal_metrics,

        productivity=productivity,

        project_progress=project_progress,
    )
def get_recent_activities(limit=5):
    """
    Retorna as atividades mais recentes.

    Args:
        limit: quantidade máxima de registros.

    Returns:
        list:
            Lista de atividades recentes.
    """

    # Buscamos as atividades mais recentes.
    activities = (
        Activity.query
        .order_by(
            Activity.created_at.desc()
        )
        .limit(limit)
        .all()
    )


    return activities