from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS usuarios (id PRIMARY KEY, nome text)")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/post")
def post(nome):
    cur.execute("INSERT INTO usuarios(nome) VALUES (?)", (nome,))
    con.commit()
    print("Usuário criado!")

@app.route("/get")
def get():
    for linha in cur.execute("SELECT * FROM usuarios"):
        print(linha)

@app.route("/update")
def update(id, nome):
    cur.execute("UPDATE usuarios SET nome =  ? WHERE id = ?", (nome, id))
    con.commit()
    print("Usuário atualizado!")

@app.route("/delete")
def delete(id):
    cur.execute("DELETE FROM usuarios WHERE id = ?" (id,))
    con.commit()
    print("Usuário deletado!")
    
        

app.run()