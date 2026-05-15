from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo</title>
        </head>
        <body>
            <h1>Currículo</h1>

            <h2>Informações Pessoais</h2>
            <ul>
                <li><strong>Nome:</strong> Pedro Henrique da Silva Bispo</li>  
                <li><strong>Endereço:</strong> Brumadinho - MG</li>
                <li><strong>Ocupação:</strong> Estudante de Técnico me Infomática</li>
                <li><strong>Email:</strong> 12401811@cotemig.com.br</li>
            </ul>

            <h2>Educação</h2>
            <ul>
                <li><strong>Instituição:</strong> Colégio Cotemig - Unidade Barroca</li>
                <li><strong>Curso:</strong> Desenvolvedor web mobile</li>
            </ul>
        </body>
        </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
