from flask import Flask, jsonify, abort

app = Flask(__name__)

livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis"},
    {"id": 2, "titulo": "O Cortiço", "autor": "Aluísio Azevedo"},
    {"id": 3, "titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis"}
]

@app.route("/livros", methods=["GET"])
def listar_livros():
    return jsonify(livros)

@app.route("/livros/<int:livro_id>", methods=["GET"])
def obter_livro(livro_id):
    livro = next((livro for livro in livros if livro["id"] == livro_id), None)
    if livro is None:
        abort(404, description="Livro não encontrado.")
    return jsonify(livro)

@app.errorhandler(404)
def nao_encontrado(error):
    return jsonify({"erro": error.description}), 404

if __name__ == "__main__":
    app.run(debug=True)
