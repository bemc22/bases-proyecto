from flask import request

# Función que toma como parámetro una lista de nombres de inputs de un formulario,
# y retorna un diccionario con los valores recibidos.
def input2data(lista):
    datos = {}
    for input in lista:
        datos[input] = request.form[input]
    return datos

def form2data(formulario):
    columnas = []
    values = []
    for i in request.form:
        columnas.append(i)
        values.append(request.form[i])

    return columnas, values


def input2dash(data):
    dashboard = dict()
    names = data[1]
    data = data[0]
    dash = [ names  ]

    for i in data:
        dash.append( [i[0] , i[1]])

    dashboard['data'] = dash
    dashboard['names'] = names

    return dashboard
