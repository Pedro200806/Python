from flask import Flask

app = Flask(__name__)


@app.route("/decorator")
def explicar_decorator():
    return """
    <h1>Decorators em Python</h1>

    <p>
    Um decorator em Python é uma função utilizada para modificar o comportamento
    de outra função sem alterar diretamente seu código.
    </p>

    <p>
    Eles servem para adicionar funcionalidades extras, como autenticação,
    logs, validações e organização do código.
    </p>

    <p>
    No Flask, decorators são muito utilizados para definir rotas.
    O exemplo <strong>@app.route('/decorator')</strong> indica que a função abaixo
    será executada quando o usuário acessar esse caminho no navegador.
    </p>
    """


if __name__ == "__main__":
    app.run(debug=True)
