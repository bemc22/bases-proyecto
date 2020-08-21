from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  text
from app import db


def consultar(nombre_tabla):
    consulta = text("SELECT * FROM " + nombre_tabla)
    data = db.engine.execute(consulta)
    data = data.fetchall()

    consulta = text("SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = " +"'" + nombre_tabla + "'")
    resul = db.engine.execute(consulta)
    resul = resul.fetchall()
    nombres = []
    for row in resul:
        nombres += row

    return data, nombres
