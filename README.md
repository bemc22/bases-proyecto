# bases-proyecto
Buenas tardes profe.

El archivo que ejecuta el servidor es "app.py".

Para poder visualizar correctamente el proyecto, es necesario instalar las siguientes librerias:
Flask
SQLAlchemy
Flask-SQLAlchemy
psycop2

Al momento de instalarlas, al ejecutar pip freeze le debería mostrar una salida más o menos similar a:
click==7.1.2
Flask==1.1.2
Flask-SQLAlchemy==2.4.4
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
psycopg2==2.8.5
SQLAlchemy==1.3.19
Werkzeug==1.0.1

Respecto a la base de datos, nosotros la manejamos online, por lo que no es necesario que haga la instalación 
en postgres local. Desde el app.py realiza la conexión.

