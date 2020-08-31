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
    return

def eliminar(nombre_tabla,id,name_id):
    eliminacion = "DELETE FROM %s WHERE %s = %s" %(nombre_tabla,name_id,id)
    db.engine.execute(eliminacion)
    return

def editar(nombre_tabla,columnas,values):
    updates = "SET"
    size = len(columnas)
    updates += ",".join(  [" %s = '%s'" % (i,j) for i,j in  zip(columnas[1:size],values[1:size])]  )
    edicion = "UPDATE  %s %s WHERE %s = %s" % (nombre_tabla,updates,columnas[0],values[0])
    db.engine.execute(edicion)
    return

# Para vistas:
def proced_vista(nombre_vista, values, funcion):
    valores =  "(" + ", ".join([ "'" + str(i) + "'" for i in values]) + ")"
    procedimiento = "CALL %s_%s%s;" % (funcion, nombre_vista, valores)
    db.engine.execute(text(procedimiento).execution_options(autocommit=True))
    return


#def editar_vista(nombre_vista, values):
