"""
Tratamento centralizado de erros HTTP.
"""


from flask import (
    jsonify,
    render_template,
    request,
)


def register_error_handlers(app):
    """
    Registra os handlers globais de erro.

    Args:
        app: instância da aplicação Flask.
    """

    @app.errorhandler(404)
    def not_found(error):
        """
        Trata páginas inexistentes.
        """

        # Se a requisição espera JSON,
        # retornamos JSON.
        if request.accept_mimetypes.best == "application/json":

            return jsonify(
                {
                    "error": "resource_not_found",
                    "message": "Recurso não encontrado.",
                }
            ), 404


        # Caso contrário, renderizamos
        # uma página HTML.
        return render_template(
            "errors/404.html"
        ), 404


    @app.errorhandler(500)
    def internal_server_error(error):
        """
        Trata erros internos do servidor.
        """

        if request.accept_mimetypes.best == "application/json":

            return jsonify(
                {
                    "error": "internal_server_error",
                    "message": "Erro interno do servidor.",
                }
            ), 500


        return render_template(
            "errors/500.html"
        ), 500