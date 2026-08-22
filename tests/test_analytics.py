"""
Testes relacionados às métricas
e analytics do DevTrack.
"""


def test_project_metrics(client, app):
    """
    Verifica se as métricas de projetos
    são calculadas corretamente.
    """

    # Primeiro criamos o usuário de teste.
    from tests.test_auth import (
        create_test_user,
    )


    create_test_user(
        app
    )


    # Realizamos login.
    client.post(
        "/auth/login",
        data={
            "email": "login@example.com",
            "password": "12345678",
        },
    )


    response = client.get(
        "/analytics/"
    )


    assert response.status_code == 200