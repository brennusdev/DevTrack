"""
Serviço responsável pelas regras de autenticação.

A camada de service concentra a lógica de negócio
relacionada a cadastro, login e identificação
do usuário autenticado.
"""

from models import User


def find_user_by_email(email):
    """
    Procura um usuário através do email.

    Args:
        email: endereço de email.

    Returns:
        User ou None.
    """

    return User.query.filter_by(
        email=email
    ).first()


def create_user(name, email, password):
    """
    Cria um novo usuário.

    Args:
        name: nome do usuário.
        email: email.
        password: senha em texto original.

    Returns:
        User criado.
    """

    user = User(
        name=name,
        email=email,
    )

    # A senha nunca é salva diretamente.
    # O método transforma a senha em hash.
    user.set_password(password)

    return user