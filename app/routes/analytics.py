"""
Rotas responsáveis pelo módulo de analytics.
"""


from flask import (
    Blueprint,
    render_template,
)


from app.services.analytics import (
    get_project_progress,
    get_study_metrics,
    get_goal_metrics,
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

    study_metrics = (
        get_study_metrics()
    )


    goal_metrics = (
        get_goal_metrics()
    )


    project_progress = (
        get_project_progress()
    )

    # --------------------------------------------------
    # RENDERIZAÇÃO
    # --------------------------------------------------

    return render_template(
        "analytics/dashboard.html",

        study_metrics=study_metrics,

        goal_metrics=goal_metrics,

        project_progress=project_progress,
    )