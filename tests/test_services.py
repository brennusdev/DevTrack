"""
Testes relacionados aos services da aplicação.
"""


from services.auth import (
    find_user_by_email,
    create_user,
)


def test_create_user(app):
    """
    Verifica se o service consegue
    construir corretamente um usuário.
    """

    with app.app_context():

        user = create_user(
            name="Developer",
            email="developer@example.com",
            password="12345678",
        )


        assert user.name == "Developer"

        assert (
            user.email
            == "developer@example.com"
        )


        # A senha deve ter sido transformada
        # em hash.
        assert (
            user.password_hash
            != "12345678"
        )
def test_find_user_by_email(app):
    """
    Verifica a busca de usuário por email.
    """

    from database.db import db
    from models import User


    with app.app_context():

        user = User(
            name="Developer",
            email="developer@example.com",
        )

        user.set_password(
            "12345678"
        )


        db.session.add(
            user
        )

        db.session.commit()


        result = find_user_by_email(
            "developer@example.com"
        )


        assert result is not None

        assert (
            result.email
            == "developer@example.com"
        )        