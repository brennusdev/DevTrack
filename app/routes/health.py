"""
Endpoint utilizado para verificar
a saúde da aplicação.
"""


from flask import (
    Blueprint,
    jsonify,
)


from .database.db import db


health_bp = Blueprint(
    "health",
    __name__,
    url_prefix="/health",
)


@health_bp.route("/")
def health_check():
    """
    Verifica se a aplicação e o banco
    estão funcionando.
    """

    database_status = "healthy"


    try:

        # Executamos uma consulta extremamente
        # simples para verificar a conexão.
        db.session.execute(
            db.text("SELECT 1")
        )


    except Exception as error:

        # Registramos o problema.
        database_status = "unhealthy"


    return jsonify(
        {
            "status": "healthy",

            "service": "devtrack",

            "database": database_status,
        }
    )