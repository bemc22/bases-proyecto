import csv


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
