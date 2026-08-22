"""
Validações reutilizáveis da aplicação.
"""


import re


def validate_email(email):
    """
    Verifica se o email possui um formato básico válido.

    Args:
        email: endereço de email.

    Returns:
        bool.
    """

    pattern = (
        r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    )


    return bool(
        re.match(
            pattern,
            email,
        )
    )


def validate_required(value):
    """
    Verifica se um valor obrigatório
    foi preenchido.

    Args:
        value: valor a ser validado.

    Returns:
        bool.
    """

    if value is None:

        return False


    return bool(
        str(value).strip()
    )


def validate_progress(progress):
    """
    Verifica se um progresso está
    entre 0 e 100.

    Args:
        progress: percentual.

    Returns:
        bool.
    """

    try:

        progress = int(
            progress
        )

    except (
        TypeError,
        ValueError,
    ):

        return False


    return 0 <= progress <= 100