"""
Modelo responsável pelo histórico de atividades.
"""

from datetime import datetime

from database.db import db


class Activity(db.Model):
    """
    Representa uma atividade realizada pelo usuário.
    """

    # Identificador único.
    id = db.Column(
        db.Integer,
        primary_key=True,
    )


    # Tipo da atividade.
    #
    # Exemplos:
    #
    # commit
    # study
    # goal
    # project
    type = db.Column(
        db.String(50),
        nullable=False,
    )


    # Título da atividade.
    title = db.Column(
        db.String(150),
        nullable=False,
    )


    # Descrição opcional.
    description = db.Column(
        db.String(255),
        nullable=True,
    )


    # Momento em que a atividade ocorreu.
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False,
    )


    def __repr__(self):
        """
        Representação textual da atividade.
        """

        return (
            f"<Activity "
            f"id={self.id} "
            f"type={self.type!r} "
            f"title={self.title!r}>"
        )