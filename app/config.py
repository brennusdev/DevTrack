"""
Configurações centrais da aplicação DevTrack.

Manter as configurações em um módulo separado
evita espalhar valores de configuração pelo projeto.
"""


class Config:
    """
    Configuração padrão da aplicação.

    Esta classe será expandida nas próximas versões
    para receber configurações de banco de dados,
    autenticação, segurança e outros componentes.
    """

    # Define uma chave secreta utilizada pelo Flask
    # para recursos que dependem de segurança,
    # como sessões e cookies assinados.
    #
    # IMPORTANTE:
    # Em produção essa chave deverá vir de uma
    # variável de ambiente e nunca ficar exposta
    # diretamente no código-fonte.
    SECRET_KEY = "devtrack-development-key"

    # Ativa o modo de desenvolvimento.
    #
    # Durante o desenvolvimento isso facilita
    # a identificação de erros.
    #
    # Mais adiante vamos separar corretamente
    # desenvolvimento e produção.
    DEBUG = True