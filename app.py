from flask import Flask, render_template, url_for, session, redirect, flash, request
from flask_sqlalchemy import SQLAlchemy

from crud import  *
from funciones import *
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
        return render_template('menu.html.j2')
    else:
        return render_template('login.html.j2')


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


@app.route('/logout', methods=['POST'])
def logout():
    if 'rol' in session:
        session.clear()
    return redirect(url_for('inicio'))

@app.route('/<nombre_tabla>')
def tabla(nombre_tabla):
    data , nombres =consultar(nombre_tabla)
    return render_template('crud.html.j2' , data=data, nombres=nombres, nombre_tabla=nombre_tabla)

@app.route('/personal/<nombre_vista>')
def vista(nombre_vista):
    data , nombres =consultar('personal_'+nombre_vista)
    return render_template('view.html.j2' , data=data, nombres=nombres, nombre_tabla=nombre_vista)

@app.route('/insert/<nombre_tabla>' , methods=['POST'])
def insert(nombre_tabla):
    if request.method == 'POST':
        columnas, values = form2data(request.form)
        insertar(nombre_tabla,columnas,values)
    return redirect(url_for('tabla' , nombre_tabla = nombre_tabla))

@app.route('/delete/<nombre_tabla>/<id>/<name_id>' , methods=['GET','POST'])
def delete(nombre_tabla, id,name_id):
    eliminar(nombre_tabla,id,name_id)
    return redirect(url_for('tabla' , nombre_tabla = nombre_tabla))

@app.route('/update/<nombre_tabla>' , methods=['GET','POST'])
def update(nombre_tabla):
    if request.method == 'POST':
        columnas, values = form2data(request.form)
        editar(nombre_tabla,columnas,values)

    return redirect(url_for('tabla' , nombre_tabla = nombre_tabla))



if __name__ == '__main__':
    app.run(debug=True, port=5000)
