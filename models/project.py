"""
Modelo responsável pelos projetos do DevTrack.

Cada objeto Project representa um projeto armazenado
no banco de dados.
"""

from datetime import datetime

from database.db import db


class Project(db.Model):
    """
    Representa um projeto dentro do sistema.

    Cada instância dessa classe representa uma linha
    da tabela projects no banco de dados.
    """

    # --------------------------------------------------
    # IDENTIFICADOR
    # --------------------------------------------------

    # Chave primária da tabela.

    # Cada projeto terá um ID único.
    id = db.Column(
        db.Integer,
        primary_key=True,
    )


    # --------------------------------------------------
    # INFORMAÇÕES DO PROJETO
    # --------------------------------------------------

    # Nome do projeto.
    name = db.Column(
        db.String(120),
        nullable=False,
    )

    # Tecnologia principal utilizada.
    technology = db.Column(
        db.String(100),
        nullable=False,
    )

    # Percentual de progresso.
    #
    # O valor esperado ficará entre 0 e 100.
    progress = db.Column(
        db.Integer,
        default=0,
        nullable=False,
    )


    # --------------------------------------------------
    # DATA
    # --------------------------------------------------

    # Registra quando o projeto foi criado.
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False,
    )


    def __repr__(self):
        """
        Representação textual do objeto.

        Útil principalmente durante debugging.
        """

        return (
            f"<Project "
            f"id={self.id} "
            f"name={self.name!r}>"
        )