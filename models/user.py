"""
Modelo responsável pelos usuários do DevTrack.

Cada usuário possui sua própria conta e,
posteriormente, seus próprios projetos, estudos,
metas e atividades.
"""

from datetime import datetime

from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)

from app.database.db import db


class User(db.Model):
    """
    Representa um usuário cadastrado no sistema.
    """

    # --------------------------------------------------
    # IDENTIFICADOR
    # --------------------------------------------------

    id = db.Column(
        db.Integer,
        primary_key=True,
    )


    # --------------------------------------------------
    # DADOS DO USUÁRIO
    # --------------------------------------------------

    name = db.Column(
        db.String(100),
        nullable=False,
    )


    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False,
        index=True,
    )


    password_hash = db.Column(
        db.String(255),
        nullable=False,
    )


    # --------------------------------------------------
    # DATA DE CRIAÇÃO
    # --------------------------------------------------

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False,
    )


    # --------------------------------------------------
    # SENHA
    # --------------------------------------------------

    def set_password(self, password):
        """
        Transforma a senha original em um hash seguro.

        A senha original nunca deve ser armazenada
        diretamente no banco de dados.

        Args:
            password: senha informada pelo usuário.
        """

        self.password_hash = (
            generate_password_hash(password)
        )


    def check_password(self, password):
        """
        Verifica se a senha informada corresponde
        ao hash armazenado.

        Args:
            password: senha informada no login.

        Returns:
            bool: True caso a senha seja válida.
        """

        return check_password_hash(
            self.password_hash,
            password,
        )