"""
Middleware responsável pela proteção das
rotas privadas do DevTrack.
"""
from middleware.auth import login_required

from functools import wraps

from flask import (
    flash,
    redirect,
    session,
    url_for,
)


def login_required(view):
    """
    Garante que determinada rota só possa
    ser acessada por usuários autenticados.

    Args:
        view: função da rota protegida.

    Returns:
        Função decorada.
    """

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        # Verificamos se existe um usuário
        # armazenado na sessão.
        if "user_id" not in session:

            flash(
                "Faça login para continuar.",
                "error",
            )

            return redirect(
                url_for("auth.login")
            )


        # Caso esteja autenticado,
        # executamos normalmente a rota.
        return view(
            *args,
            **kwargs,
        )


    return wrapped_view