"""
Testes de integração do DevTrack.

Aqui verificamos fluxos completos envolvendo
mais de uma camada da aplicação.
"""


def test_complete_user_flow(client, app):
    """
    Testa o fluxo:

    cadastro
        ↓
    login
        ↓
    acesso ao dashboard
        ↓
    logout
    """

    # --------------------------------------------------
    # CADASTRO
    # --------------------------------------------------

    response = client.post(
        "/auth/register",
        data={
            "name": "Integration User",
            "email": "integration@example.com",
            "password": "12345678",
        },
    )


    assert response.status_code == 302


    # --------------------------------------------------
    # LOGIN
    # --------------------------------------------------

    response = client.post(
        "/auth/login",
        data={
            "email": "integration@example.com",
            "password": "12345678",
        },
    )


    assert response.status_code == 302


    # --------------------------------------------------
    # DASHBOARD
    # --------------------------------------------------

    response = client.get(
        "/dashboard/"
    )


    assert response.status_code == 200


    # --------------------------------------------------
    # LOGOUT
    # --------------------------------------------------

    response = client.get(
        "/auth/logout"
    )


    assert response.status_code == 302