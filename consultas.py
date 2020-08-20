from flaskext.mysql import MySQL


def consultar(nombre_tabla, cursor):
    consulta = "SELECT * FROM " + nombre_tabla
    cursor.execute(consulta)

    data = cursor.fetchall()

    consulta = "SHOW COLUMNS FROM " + nombre_tabla
    cursor.execute(consulta)
    nombres = ()
    for row in cursor.fetchall():
        nombres += (row[0],)

    return data, nombres
