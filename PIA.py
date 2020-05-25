import pandas as pd
import numpy as np


op = 0
alumno = {}
Matricula = []
calificaciones = []
materias = []

while (op!=5):
    
    print("2.-Registrar Materia")
    print("3.-Registrar Calificacion")
    print("4.-Mostrar registro")
    print("5.-Salir del menu")
    op = int(input("Dame La Opcion:"))
    if (op==1):
        for nombres in range(0,3):
            print("Registrar Alumno")
            Matricula.append(input("Matricula: "))
            Nombre = input("Nombre Completo: ")
            alumno[Nombre]= []
    if (op==2):
        mat = 0
        if mat == 0:
            mat = int(input("Cuantas materias quieres registrar: "))
            print(" ")
        if mat >= 5:
            for i in range(0,mat):
                nom = input ("Nombre de la materia: ")
                materias.append(nom)
                Alumn_materia = 0
                print(" ")
        else:
             print("Mínimo 5 materias")
    if (op==3):
        numero = 0
        for a in alumno:
            numero = numero + 1
            print("**")
            print("Alumno.",numero)
            print("Nombre:",a)
            for e in materias:
                print("Materia:",e)
                calif = 0
                calif = int(input("Calificacion: "))
                alumno[a].append(calif)
                print(" ")
                
    if (op==4):
        print("Menu2 para ver calificaciones o promedios o alumnos con materias reprobadas")
        datos = pd.DataFrame(alumno)
        datos.index= [materias]
        print(" ")
        print("*******")
        print("MENU MOSTRAR")
        print("1) Mostrar todos los registros")
        print("2) Calificaciones en orden")
        print("3) Promedio de calificaciones y materia")
        print("4) Alumnos con materias reprobadas")
        print("5) Guardar reporte estadistico")
        opcion = input("Elige una opcion: ")
        print("*******")
        if opcion == "1":
            print()
            for i in Matricula,alumno,materias,calif:   
                print(i)
                print()
        elif opcion == "2":
            print()
            print("calificaciones")
            print(datos.T)
            print()
        elif opcion == "3":
            print()
            print("PROMEDIO MATERIAS")
            print(datos.T.mean())
            print()
            
        elif opcion == "4":
            print("Alumnos Con Materias Reprobadas")
            extraerAlum = alumno.keys() #Retorna una lista de elementos, los cuales serán las claves de nuestro diccionario.
            for a in extraerAlum:
                 extraer = alumno.get(a,())#Recibe como parámetro una clave, devuelve el valor de la clave. Si no lo encuentra, devuelve un objeto none.
                 print(" ")
                 print("Alumno:",a)
                 print("Calificaciones Reprobadas")
                 for o in extraer:
                     if o < 70:
                         print(o)
                         
        elif opcion == "5":
            archivo = open('Reporte Estadistico.txt','a')
            archivo.write('REPORTE POR MATERIA\n')
            rep_por_alumn = str(datos.T.describe())
            archivo.write(rep_por_alumn)
            archivo.write(' \n')
            archivo.write(' \n')
            archivo.write('REPORTE POR ALUMNO\n')
            for e in alumno:
                describiendo = datos[e].describe()
                print(describiendo)
                enstr = str(describiendo)
                archivo.write(enstr)
            print(" ")
            print("Reporte Generado con éxito!")
            archivo.close()
        else:
            print("Escoga una opcion correcta")
        
        
 
    if (op== 6):
        print("Salir del Menu.!Gracias por utilizar el menu!")