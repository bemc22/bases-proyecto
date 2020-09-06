from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  text
from app import db

# Comentario , Comentario editado

def consultar(nombre_tabla, clave=None, valor=None):
    if clave and valor:
        consulta = text(f"SELECT * FROM {nombre_tabla} WHERE {clave} = {valor}")
    else:
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

def foreign(nombre_tabla, clave=None, valor=None, campos=None):
    if not campos:
        campos = [f"{nombre_tabla}_id", "nombre"]
    campos = ', '.join(campos)
    if clave and valor:
        if type(valor) is list:
            valor = ', '.join([str(v) for v in valor])
        consulta = text(f"SELECT {campos} FROM {nombre_tabla} WHERE {clave} in ({valor})")
    else:
        consulta = text(f"SELECT {campos} FROM {nombre_tabla}")
    data = db.engine.execute(consulta)
    data = data.fetchall()
    return data

# Para vistas:
def proced_vista(nombre_vista, values, funcion):
    valores =  "(" + ", ".join([ "'" + str(i) + "'" for i in values]) + ")"
    procedimiento = "CALL %s_%s%s;" % (funcion, nombre_vista, valores)
    db.engine.execute(text(procedimiento).execution_options(autocommit=True))
    return


# Para Profesor curso (materias, grupos):

def proced_curso(values, nombre_tabla):
    valores = "(" + ", ".join([ "'" + str(i) + "'" for i in values]) + ")"
    procedimiento ="CALL curso"
    return
