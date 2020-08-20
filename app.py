from flask import Flask, render_template, url_for
from flaskext.mysql import MySQL
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

    return render_template('index.html.jinja')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
