"""
Funções auxiliares relacionadas ao usuário autenticado.
"""

from flask import session

from models import User


def get_current_user():
    """
    Retorna o usuário atualmente autenticado.

    Returns:
        User ou None.
    """

    # Recuperamos o ID armazenado na sessão.
    user_id = session.get(
        "user_id"
    )


    # Se não houver usuário na sessão,
    # não existe usuário autenticado.
    if user_id is None:

        return None


    # Procuramos o usuário no banco.
    return User.query.get(
        user_id
    )