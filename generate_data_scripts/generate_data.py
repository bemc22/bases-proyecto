import csv
from random import *


def generar_persona():
    persona = [];
    with open('data.csv') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=",")
        id = 1;
        for row in csvreader:
            nombre = row[0]
            apellido = row[1]
            sexo = row[2][0]
            fecha= row[3].split("/")
            fecha_nacimiento = fecha[2] + "-" + fecha[0] + "-" + fecha[1]
            insert = '(' + str(id) + ',"' + nombre + '","' + apellido + '","' + sexo + '","' + fecha_nacimiento + '"),'
            id += 1
            persona.append(insert)


    for i in persona:
        print(i)


def generar_carrera():

    carrera = ["INGENIERIA INDUSTRIAL" , "INGENIERIA DE SISTEMAS" , "INGENIERIA CIVIL" , "INGENIERIA MECANICA"]
     id = 1
    for i in carrera:
        row =  '(' + str(id) + ',"' + i + '"),'
        id +=1
        print(row)

import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def generar_roles():
    estudiantes = []
    for i in range(1,5101):
        estudiantes.append(i)
    profesor = sample(ids,100)
    for i in profesor:
        estudiantes.remove(i)

    id = 1

    print("Tabla profesores")
    for j in profesor:
        rng = random.random()
        if rng >= 0.6:
            depen = 'P'
        else:
            depen = 'C'


        row = '(' + str(id) + ',' + str(j) + ",'" + depen + "'," + '"' + get_random_string(8) + '"),'
        print(row)
        id += 1

    id = 1
    for j in estudiantes:
        rng = random.random()
        if rng <= 0.1:
            carrera = 4
        elif rng <= 0.2:
            carrera = 3
        elif rng <= 0.3:
            carrera = 2
        else:
            carrera = 1
        semestre = random.randint(6, 10)

        row = '(' + str(id) + ',' + str(j) + ',' + str(carrera) + ',' + str(semestre) + '),'
        print(row)
        id += 1


generar_roles()
