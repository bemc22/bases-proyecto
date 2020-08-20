from flask import Flask, render_template, url_for
from flaskext.mysql import MySQL
from consultas import  *
app = Flask(__name__)

# configuracion de conexion
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'galea'


mysql = MySQL()
mysql.init_app(app)


@app.route('/')
def inicio():
    return render_template('header.html.jinja')

@app.route('/<nombre_tabla>')
def tabla(nombre_tabla):

    cursor = mysql.get_db().cursor()
    data, nombres = consultar(nombre_tabla,cursor)
    print(nombres)
    print(nombre_tabla)

    return render_template('crud.html.jinja' , data=data, nombres=nombres, nombre_tabla=nombre_tabla)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
