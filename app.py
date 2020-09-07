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

# Rutas

@app.route('/')
def inicio():
    if "rol" in session:

        dash = consultar('dash_admin')
        dash = input2dash(dash)

        print(dash)
        return render_template('menu.html.j2' , dash= dash)
    else:
        carreras = consultar('carrera')
        categorias = [c[1] for c in consultar('categoria')[0]]
        return render_template('login.html.j2', carreras= carreras[0], categorias=categorias)

# Login

@app.route('/login', methods=['POST'])
def login():
    datos = input2data(["usuario", "clave", "rol"])
    consulta = text("SELECT * FROM usuario_"+datos["rol"]+" WHERE nombre = '"+datos["usuario"]+"' AND clave = '"+datos["clave"]+"'")
    data = db.engine.execute(consulta)
    data = data.fetchone()
    if data:
        session["rol"] = datos["rol"]
        if datos["rol"] == 'profesor':
            session["id"] = data[2]
        elif datos["rol"] == 'auxiliar':
            session["id"] = data[2]
            session["jefe"] = data[3]
        flash("Ha ingresado correctamente al sistema.", 'success')
    else:
        flash("El usuario y la contraseña no coinciden", 'error')
    return redirect(url_for('inicio'))

@app.route('/logout', methods=['POST'])
def logout():
    if 'rol' in session:
        session.clear()
    return redirect(url_for('inicio'))

@app.route('/registro', methods=['POST'])
def registro():
    columnas, values = form2data(request.form)
    consulta = text(f"SELECT 1 FROM estudiante WHERE codigo = '{values[0]}'")
    verifica = db.engine.execute(consulta)
    verifica = verifica.fetchone()
    if verifica:
        flash('El estudiante ya se encuentra registrado en el sistema.', 'error')
    else:
        proced_vista('estudiante',values,'inserta')
        flash('El registro ha sido exitoso, ya puede confirmar su asistencia', 'success')
    return redirect(url_for('inicio'))

@app.route('/asist', methods=['post'])
def asist():
    columnas, values = form2data(request.form)
    proced_vista('ludica',values[:2],'asistencia')
    for i,v in enumerate(values[2:]):
        proced_vista('nota',[values[1], i+1, v],'inserta')
    flash('Su asistencia ha sido guardada exitosamente', 'success')
    return redirect(url_for('inicio'))

# CRUD para cualquier tabla

@app.route('/<nombre_tabla>')
def tabla(nombre_tabla):
    if 'rol' in session:
        data , nombres =consultar(nombre_tabla)
        return render_template('crud.html.j2' , data=data, nombres=nombres, nombre_tabla=nombre_tabla)
    else:
        return redirect(url_for('inicio'))

@app.route('/insert/<nombre_tabla>' , methods=['POST'])
def insert(nombre_tabla):
    if 'rol' in session:
        if request.method == 'POST':
            columnas, values = form2data(request.form)
            insertar(nombre_tabla,columnas,values)
            flash('El registro ha sido guardado exitosamente.', 'info')
        return redirect(url_for('capacitaciones')) if nombre_tabla=='capacitacion_auxiliar' else redirect(url_for('tabla' , nombre_tabla = nombre_tabla))
    else:
        return redirect(url_for('inicio'))

@app.route('/delete/<nombre_tabla>/<id>/<name_id>' , methods=['GET','POST'])
def delete(nombre_tabla, id,name_id):
    if 'rol' in session:
        eliminar(nombre_tabla,id,name_id)
        flash('El registro ha sido eliminado exitosamente.', 'info')
        return redirect(url_for('tabla' , nombre_tabla = nombre_tabla))
    else:
        return redirect(url_for('inicio'))

@app.route('/update/<nombre_tabla>' , methods=['GET','POST'])
def update(nombre_tabla):
    if 'rol' in session:
        if request.method == 'POST':
            columnas, values = form2data(request.form)
            editar(nombre_tabla,columnas,values)
            flash('El registro ha sido editado exitosamente.', 'info')
        return redirect(url_for('tabla' , nombre_tabla = nombre_tabla))
    else:
        return redirect(url_for('inicio'))

# Rol: Profesor Cursos

@app.route('/curso/<nombre_tabla>')
def curso(nombre_tabla):
    if 'rol' in session:
        if session['rol'] == "profesor":
            materias , x = consultar('materia')
            mis_materias , x = consultar('curso_'+'materia' , session['rol'] + '_id' , session['id'])
            dict_materias =dict()
            for materia in mis_materias:
                dict_materias[materia[0]] = materia[2]

            data , nombres =consultar('curso_'+nombre_tabla , session['rol'] + '_id' , session['id'])
            return render_template('profesor.html.j2' , data=data, nombres=nombres[:-2], nombre_tabla=nombre_tabla , mis_materias=dict_materias, materias=materias )
    else:
        return redirect(url_for('inicio'))

@app.route('/curso/insert/<nombre_tabla>', methods=['POST'])
def function_curso(nombre_tabla):
    if 'rol' in session:
        if request.method == 'POST':
            print(request.form)
            columnas , values = form2data(request.form)
            values = [str(session['id'])] + values
            proced_vista('curso_' + nombre_tabla, values , 'inserta')
            flash('El curso ha sido insertado exitosamente.', 'info')
            return redirect(url_for('curso' , nombre_tabla = nombre_tabla))
    else:
        return redirect(url_for('inicio'))

@app.route('/curso/delete/<nombre_tabla>/<id>', methods=['GET','POST'])
def curso_delete(nombre_tabla,id):
    if 'rol' in session:
        if nombre_tabla == 'materia':
            eliminar('materia_profesor', id, 'mp_id' )
        elif nombre_tabla == 'grupo':
            eliminar('grupo' , id , 'grupo_id')
        flash('El curso ha sido eliminado exitosamente.', 'info')
        return redirect(url_for('curso' , nombre_tabla = nombre_tabla))
    else:
        return redirect(url_for('inicio'))

# Capacitaciones:
@app.route('/capacitaciones')
def capacitaciones():
    if 'rol' in session:
        data , nombres =consultar('capacitaciones')
        ludicas = foreign('ludica')
        return render_template('capacitacion.html.j2', data=data, nombres=nombres, ludicas=ludicas)
    else:
        return redirect(url_for('inicio'))


# Vistas:
@app.route('/personal/<nombre_vista>')
def vista(nombre_vista):
    if 'rol' in session:
        col_select = {
        'sexo':[('M','Masculino'),('F','Femenino')] ,
        'dependencia': [('C','Catedra'),('P','Planta')],
        'cargo': [('true','Jefe') , ('false','Auxiliar')]
        }

        carreras = consultar('carrera')
        col_select['carrera'] = carreras[0]

        data , nombres =consultar('personal_'+nombre_vista)
        return render_template('view.html.j2' , data=data, nombres=nombres, nombre_tabla=nombre_vista, especial_case=col_select)
    else:
        return redirect(url_for('inicio'))

@app.route('/sesiones')
def sesiones():
    if 'rol' in session:
        if session['rol'] == 'admin':
            data , nombres =consultar('sesiones_'+session['rol'])
            auxiliares = consultar('ver_auxiliar')
        else:
            data , nombres =consultar('sesiones_'+session['rol'], session['rol']+'_id', session['id'])
        if session['rol'] == "profesor":
            ludicas = foreign('ludica')
            mp = foreign('materia_profesor', 'profesor_id', session['id'], ['*'])
            grupos = foreign('grupo', 'mp_id', [m[0] for m in mp])
            return render_template('sesion.html.j2' , data=[reg[:-1] for reg in data], nombres=nombres[:-1], ludicas=ludicas, grupos=grupos)
        elif session['rol'] == "auxiliar":
            return render_template('sesion.html.j2' , data=[reg[:-1] for reg in data], nombres=nombres[:-1])
        else:

            return render_template('sesion.html.j2' , data=data, nombres=nombres , auxiliares=auxiliares)
    else:
        return redirect(url_for('inicio'))

@app.route('/sesiones/asignar' , methods=['POST'])
def asignar():
    if 'rol' in session:
        if request.method == 'POST':
            columnas, values = form2data(request.form)
            insertar('auxiliar_sesion',columnas,values)
            flash('El auxiliar ha sido guardado exitosamente.', 'info')
        return redirect(url_for('sesiones'))
    else:
        return redirect(url_for('inicio'))


@app.route('/<funcion>/<nombre_vista>', methods=['POST'])
def function_vista(nombre_vista, funcion):
    if 'rol' in session:
        if request.method == 'POST':
            columnas, values = form2data(request.form)
            proced_vista(nombre_vista,values,funcion)
        flash(f'El registro ha sido {funcion}do exitosamente.', 'info')
        return redirect(url_for(f'{nombre_vista}es')) if nombre_vista in ['sesion', 'capacitacion'] else  redirect(url_for('vista' , nombre_vista = nombre_vista))
    else:
        return redirect(url_for('inicio'))

@app.route('/delete/personal/<nombre_tabla>/<id>/<name_id>' , methods=['GET','POST'])
def delete_vista(nombre_tabla, id,name_id):
    if 'rol' in session:
        eliminar(nombre_tabla,id,name_id)
        flash('El registro ha sido eliminado exitosamente.', 'info')
        return redirect(url_for('vista' , nombre_vista = nombre_tabla))
    else:
        return redirect(url_for('inicio'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
