"""
Rotas relacionadas à autenticação.

Este módulo contém:

- cadastro;
- login;
- logout.
"""
from flask import session
@auth_bp].route(
    "/login",
    methods=["GET", "POST"],
)
def login():
    """
    Realiza o login de um usuário existente.
    """

    if request.method == "POST":

        email = request.form.get(
            "email",
            "",
        ).strip().lower()

        password = request.form.get(
            "password",
            "",
        )


        # Procuramos o usuário.
        user = find_user_by_email(
            email
        )


        # Verificamos usuário e senha.
        if (
            user is None
            or not user.check_password(password)
        ):

            flash(
                "Email ou senha inválidos.",
                "error",
            )

            return render_template(
                "auth/login.html"
            )


        # --------------------------------------------------
        # CRIAÇÃO DA SESSÃO
        # --------------------------------------------------

        session.clear()


        session["user_id"] = user.id


        flash(
            "Login realizado com sucesso!",
            "success",
        )


        return redirect(
            url_for("dashboard.dashboard")
        )


    return render_template(
        "auth/login.html"
    )

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from database.db import db

from services.auth import (
    create_user,
    find_user_by_email,
)


auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
)


@auth_bp.route(
    "/register",
    methods=["GET", "POST"],
)
def register():
    """
    Realiza o cadastro de um novo usuário.
    """

    if request.method == "POST":

        # Recuperamos os dados enviados.
        name = request.form.get(
            "name",
            "",
        ).strip()

        email = request.form.get(
            "email",
            "",
        ).strip().lower()

        password = request.form.get(
            "password",
            "",
        )


        # --------------------------------------------------
        # VALIDAÇÕES
        # --------------------------------------------------

        if not name:

            flash(
                "Informe seu nome.",
                "error",
            )

            return render_template(
                "auth/register.html"
            )


        if not email:

            flash(
                "Informe seu email.",
                "error",
            )

            return render_template(
                "auth/register.html"
            )


        if not password:

            flash(
                "Informe uma senha.",
                "error",
            )

            return render_template(
                "auth/register.html"
            )


        if len(password) < 8:

            flash(
                "A senha deve possuir pelo menos 8 caracteres.",
                "error",
            )

            return render_template(
                "auth/register.html"
            )


        # Verificamos se já existe uma conta.
        existing_user = find_user_by_email(
            email
        )


        if existing_user:

            flash(
                "Este email já está cadastrado.",
                "error",
            )

            return render_template(
                "auth/register.html"
            )


        # Criamos o usuário.
        user = create_user(
            name=name,
            email=email,
            password=password,
        )


        # Salvamos no banco.
        db.session.add(user)

        db.session.commit()


        flash(
            "Conta criada com sucesso!",
            "success",
        )


        return redirect(
            url_for("auth.login")
        )


    return render_template(
        "auth/register.html"
    )
    @auth_bp.route("/logout")
def logout():
    """
    Encerra a sessão do usuário.
    """

    # Remove todos os dados armazenados
    # na sessão atual.
    session.clear()


    flash(
        "Você saiu da sua conta.",
        "success",
    )


    return redirect(
        url_for("auth.login")
    )