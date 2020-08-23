from flask import Flask, render_template, url_for, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy

from consultas import  *
from formularios import *
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# configuracion de conexion
url = "postgres://qowtdwog:eXh8ZCIrCaJXQmjTJvRx_Ukv3uvmYG7A@lallah.db.elephantsql.com:5432/qowtdwog"
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/')
def inicio():

    if "rol" in session:
        return render_template('menu.html.jinja')
    else:
        return render_template('login.html.jinja')


@app.route('/login', methods=['POST'])
def login():

    datos = input2data(["usuario", "clave", "rol"])
    consulta = text("SELECT * FROM usuario_"+datos["rol"]+" WHERE nombre = '"+datos["usuario"]+"' AND clave = '"+datos["clave"]+"'")
    data = db.engine.execute(consulta)
    data = data.fetchone()
    print(data)
    if data:
        session["rol"] = datos["rol"]
    else:
        flash("El usuario y la contraseña no coinciden")
    return redirect(url_for('inicio'))


@app.route('/logout', methods=['post'])
def logout():

    if 'rol' in session:
        session.clear()
    return redirect(url_for('inicio'))



@app.route('/<nombre_tabla>')
def tabla(nombre_tabla):

    data , nombres =consultar(nombre_tabla)
    return render_template('crud.html.jinja' , data=data, nombres=nombres, nombre_tabla=nombre_tabla)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
