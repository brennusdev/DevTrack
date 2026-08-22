"""
Testes relacionados ao sistema de autenticação.
"""


from models import User


def test_user_registration(client, app):
    """
    Verifica se um usuário consegue
    criar uma conta.
    """

    response = client.post(
        "/auth/register",
        data={
            "name": "Test User",
            "email": "test@example.com",
            "password": "12345678",
        },
        follow_redirects=True,
    )


    # A requisição deve ser processada
    # com sucesso.
    assert response.status_code == 200


    # Verificamos se o usuário realmente
    # foi criado no banco.
    with app.app_context():

        user = User.query.filter_by(
            email="test@example.com"
        ).first()


        assert user is not None


        # A senha não deve ser armazenada
        # diretamente.
        assert user.password_hash != "12345678"
        
def create_test_user(app):
            
    """
    Cria um usuário específico para os testes.
    """

    from database.db import db

    user = User(
        name="Test User",
        email="login@example.com",
    )

    user.set_password(
        "12345678"
    )

    db.session.add(user)

    db.session.commit()

    return user

def test_user_login(client, app):
    """
    Verifica se um usuário consegue
    realizar login.
    """

    create_test_user(
        app
    )


    response = client.post(
        "/auth/login",
        data={
            "email": "login@example.com",
            "password": "12345678",
        },
        follow_redirects=True,
    )


    assert response.status_code == 200

def test_invalid_login(client, app):
    """
    Verifica se o sistema rejeita
    credenciais inválidas.
    """

    create_test_user(
        app
    )


    response = client.post(
        "/auth/login",
        data={
            "email": "login@example.com",
            "password": "senha-incorreta",
        },
    )


    assert response.status_code == 200    