"""
Ponto de entrada da aplicação DevTrack.

Este arquivo é responsável apenas por iniciar
a aplicação.

A lógica da aplicação permanece dentro do pacote app.
"""

from app import create_app


# Criamos a aplicação utilizando a Application Factory.
app = create_app()


# Este bloco verifica se o arquivo está sendo
# executado diretamente.
#
# Dessa maneira, o servidor só será iniciado
# quando executarmos:
#
# python run.py
if __name__ == "__main__":

    # Iniciamos o servidor de desenvolvimento.
    #
    # debug=True permite que alterações no código
    # sejam detectadas automaticamente e facilita
    # a visualização de erros durante o desenvolvimento.
    app.run(debug=True)