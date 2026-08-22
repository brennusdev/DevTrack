"""
Configuração do sistema de logging
do DevTrack.
"""


import logging


def configure_logging(app):
    """
    Configura o sistema de logging da aplicação.

    Args:
        app: instância Flask.
    """

    # --------------------------------------------------
    # LOGGER
    # --------------------------------------------------

    logger = logging.getLogger(
        "devtrack"
    )


    # Definimos o nível mínimo de mensagens.
    logger.setLevel(
        logging.INFO
    )


    # --------------------------------------------------
    # HANDLER
    # --------------------------------------------------

    handler = logging.StreamHandler()


    # --------------------------------------------------
    # FORMAT
    # --------------------------------------------------

    formatter = logging.Formatter(
        "[%(asctime)s] "
        "%(levelname)s "
        "%(name)s: "
        "%(message)s"
    )


    handler.setFormatter(
        formatter
    )


    # Evitamos adicionar o mesmo
    # handler diversas vezes.
    if not logger.handlers:

        logger.addHandler(
            handler
        )


    # Registramos o logger no Flask.
    app.logger.handlers = logger.handlers

    app.logger.setLevel(
        logging.INFO
    )