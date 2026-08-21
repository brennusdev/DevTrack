"""
Rotas responsáveis pelo gerenciamento de metas.
"""

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from app.database.db import db
from app.models import Goal


goals_bp = Blueprint(
    "goals",
    __name__,
    url_prefix="/goals",
)


@goals_bp.route("/")
def list_goals():
    """
    Lista todas as metas.
    """

    goals = (
        Goal.query
        .order_by(Goal.created_at.desc())
        .all()
    )

    return render_template(
        "goals/list.html",
        goals=goals,
    )


@goals_bp.route(
    "/create",
    methods=["GET", "POST"],
)
def create_goal():
    """
    Cria uma nova meta.
    """

    if request.method == "POST":

        title = request.form.get(
            "title",
            "",
        ).strip()


        if not title:

            flash(
                "O título da meta é obrigatório.",
                "error",
            )

            return render_template(
                "goals/form.html"
            )


        goal = Goal(
            title=title,
            progress=0,
            completed=False,
        )


        db.session.add(goal)

        db.session.commit()


        flash(
            "Meta criada com sucesso!",
            "success",
        )


        return redirect(
            url_for("goals.list_goals")
        )


    return render_template(
        "goals/form.html"
    )


@goals_bp.route(
    "/<int:goal_id>/progress",
    methods=["POST"],
)
def update_goal_progress(goal_id):
    """
    Atualiza o progresso de uma meta.
    """

    goal = db.get_or_404(
        Goal,
        goal_id,
    )


    progress_value = request.form.get(
        "progress",
        "0",
    ).strip()


    try:

        progress = int(progress_value)

    except ValueError:

        flash(
            "O progresso precisa ser um número inteiro.",
            "error",
        )

        return redirect(
            url_for("goals.list_goals")
        )


    if progress < 0 or progress > 100:

        flash(
            "O progresso deve estar entre 0 e 100.",
            "error",
        )

        return redirect(
            url_for("goals.list_goals")
        )


    # Atualizamos o progresso.
    goal.progress = progress


    # Se chegou a 100%, consideramos a meta concluída.
    goal.completed = progress == 100


    db.session.commit()


    flash(
        "Progresso atualizado!",
        "success",
    )


    return redirect(
        url_for("goals.list_goals")
    )


@goals_bp.route(
    "/<int:goal_id>/delete",
    methods=["POST"],
)
def delete_goal(goal_id):
    """
    Exclui uma meta.
    """

    goal = db.get_or_404(
        Goal,
        goal_id,
    )


    db.session.delete(goal)

    db.session.commit()


    flash(
        "Meta excluída.",
        "success",
    )


    return redirect(
        url_for("goals.list_goals")
    )