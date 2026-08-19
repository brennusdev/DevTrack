"""
Modelo responsável pelos registros de estudo.
"""

from datetime import datetime

from database.db import db


class Study(db.Model):
    """
    Representa uma sessão de estudo.
    """

    # Chave primária.
    id = db.Column(
        db.Integer,
        primary_key=True,
    )


    # Nome da tecnologia estudada.
    technology = db.Column(
        db.String(100),
        nullable=False,
    )


    # Quantidade de horas estudadas.
    hours = db.Column(
        db.Float,
        nullable=False,
    )


    # Título ou descrição do estudo.
    description = db.Column(
        db.String(255),
        nullable=False,
    )


    # Data em que o estudo foi criado.
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False,
    )


    def __repr__(self):
        """
        Retorna uma representação legível do estudo.
        """

        return (
            f"<Study "
            f"id={self.id} "
            f"technology={self.technology!r} "
            f"hours={self.hours}>"
        )