from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  text
from app import db

# Comentario , Comentario editado

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

def insertar(nombre_tabla, columnas,values):
    cols =  "(" + ", ".join([i for i in columnas]) + ")"
    valores =  "(" + ", ".join([ "'" + str(i) + "'" for i in values]) + ")"
    insert_into = "INSERT INTO %s %s VALUES %s" % (nombre_tabla, cols,valores)
    db.engine.execute(insert_into)

    print(insert_into)
    return 0

def eliminar(nombre_tabla,id,name_id):
    eliminacion = "DELETE FROM %s WHERE %s = %s" %(nombre_tabla,name_id,id)
    db.engine.execute(eliminacion)
    print(eliminacion)

    return 0
