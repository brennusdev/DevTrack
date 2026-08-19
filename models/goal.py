"""
Modelo responsável pelas metas do DevTrack.
"""

from datetime import datetime

from database.db import db


class Goal(db.Model):
    """
    Representa uma meta cadastrada no sistema.
    """

    # Identificador único.
    id = db.Column(
        db.Integer,
        primary_key=True,
    )


    # Nome da meta.
    title = db.Column(
        db.String(150),
        nullable=False,
    )


    # Percentual de progresso da meta.
    progress = db.Column(
        db.Integer,
        default=0,
        nullable=False,
    )


    # Indica se a meta foi concluída.
    completed = db.Column(
        db.Boolean,
        default=False,
        nullable=False,
    )


    # Data de criação.
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False,
    )


    def __repr__(self):
        """
        Retorna uma representação textual da meta.
        """

        return (
            f"<Goal "
            f"id={self.id} "
            f"title={self.title!r}>"
        )