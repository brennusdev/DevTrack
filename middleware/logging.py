"""
Configuração de logging do DevTrack.
"""
import logging


def configure_logging(app):
    """
    Configura o logging básico da aplicação.

    Args:
        app: instância da aplicação Flask.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s",
    )

    app.logger.info("DevTrack iniciado.")
