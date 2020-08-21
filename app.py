from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

from consultas import  *
app = Flask(__name__)

# configuracion de conexion
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://qowtdwog:eXh8ZCIrCaJXQmjTJvRx_Ukv3uvmYG7A@lallah.db.elephantsql.com:5432/qowtdwog"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/')
def inicio():
    return render_template('menu.html.jinja')

@app.route('/<nombre_tabla>')
def tabla(nombre_tabla):

    data , nombres =consultar(nombre_tabla)
    return render_template('crud.html.jinja' , data=data, nombres=nombres, nombre_tabla=nombre_tabla)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
