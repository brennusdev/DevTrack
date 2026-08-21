"""
Rotas responsáveis pelo gerenciamento dos estudos.
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
from app.models import Study


studies_bp = Blueprint(
    "studies",
    __name__,
    url_prefix="/studies",
)


@studies_bp.route("/")
def list_studies():
    """
    Lista todos os estudos.
    """

    studies = (
        Study.query
        .order_by(Study.created_at.desc())
        .all()
    )

    return render_template(
        "studies/list.html",
        studies=studies,
    )


@studies_bp.route(
    "/create",
    methods=["GET", "POST"],
)
def create_study():
    """
    Cria uma nova sessão de estudo.
    """

    if request.method == "POST":

        technology = request.form.get(
            "technology",
            "",
        ).strip()

        description = request.form.get(
            "description",
            "",
        ).strip()

        hours_value = request.form.get(
            "hours",
            "0",
        ).strip()


        # Validação.
        if not technology:

            flash(
                "Informe a tecnologia estudada.",
                "error",
            )

            return render_template(
                "studies/form.html"
            )


        if not description:

            flash(
                "Informe uma descrição.",
                "error",
            )

            return render_template(
                "studies/form.html"
            )


        try:

            hours = float(hours_value)

        except ValueError:

            flash(
                "As horas precisam ser um número.",
                "error",
            )

            return render_template(
                "studies/form.html"
            )


        if hours <= 0:

            flash(
                "As horas precisam ser maiores que zero.",
                "error",
            )

            return render_template(
                "studies/form.html"
            )


        # Criamos o objeto.
        study = Study(
            technology=technology,
            hours=hours,
            description=description,
        )


        # Adicionamos à sessão.
        db.session.add(study)


        # Persistimos no banco.
        db.session.commit()


        flash(
            "Estudo registrado com sucesso!",
            "success",
        )


        return redirect(
            url_for("studies.list_studies")
        )


    return render_template(
        "studies/form.html"
    )


@studies_bp.route(
    "/<int:study_id>/delete",
    methods=["POST"],
)
def delete_study(study_id):
    """
    Exclui um registro de estudo.
    """

    study = db.get_or_404(
        Study,
        study_id,
    )


    db.session.delete(study)

    db.session.commit()


    flash(
        "Registro de estudo excluído.",
        "success",
    )


    return redirect(
        url_for("studies.list_studies")
    )