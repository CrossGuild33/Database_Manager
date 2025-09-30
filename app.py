from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    con = sqlite3.connect("data.db")
    con.row_factory = sqlite3.Row
    return con

@app.route("/")
def home():
    return "Home - CRUD de Usuários"

@app.route("/post", methods=["POST"])
def post():
    nome = request.form.get("nome")
    if not nome:
        return jsonify({"error": "Nome inválido"}), 400

    con = get_db()
    cur = con.cursor()
    cur.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome,))
    con.commit()
    con.close()
    return jsonify({"message": "Usuário criado!"}), 201

@app.route("/get", methods=["GET"])
def get():
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM usuarios")
    usuarios = cur.fetchall()
    con.close()
    return jsonify([dict(u) for u in usuarios])

@app.route("/update", methods=["POST"])
def update():
    id = request.form.get("id")
    nome = request.form.get("nome")
    if not id or not nome:
        return jsonify({"error": "Dados inválidos"}), 400

    con = get_db()
    cur = con.cursor()
    cur.execute("UPDATE usuarios SET nome=? WHERE id=?", (nome, id))
    con.commit()
    con.close()
    return jsonify({"message": "Usuário atualizado!"})

@app.route("/delete", methods=["POST"])
def delete():
    id = request.form.get("id")
    if not id:
        return jsonify({"error": "ID inválido"}), 400

    con = get_db()
    cur = con.cursor()
    cur.execute("DELETE FROM usuarios WHERE id=?", (id,))
    con.commit()
    con.close()
    return jsonify({"message": "Usuário deletado!"})

if __name__ == "__main__":
    con = get_db()
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")
    con.commit()
    con.close()
    app.run(debug=True)
