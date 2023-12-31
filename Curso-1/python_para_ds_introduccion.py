# -*- coding: utf-8 -*-
"""Python para DS - Introduccion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D6tQi1LexiwgRFv9QL-BKzkhuKR8J4u5

#Python para DS - Introduccion para el lenguaje**
"""

1 + 1

'cristian'

nombre = 'cristian'

nombre

edad  = 30

edad

"""mi primera funcion"""

print ('el nombre es cristian y su edad es 29 años')

print (f'el nombre es {nombre} y su edad es {edad} años')

def saludar():
  nombre = input('digite su nombre: ')
  print (f'hola {nombre} sea bienvenido !!!')

saludar()

"""parametros"""

nombre = 'andrea'

def saludar_con_parametros(nombre):
  print(f'hola {nombre} sea bienvenid@!!!')

saludar_con_parametros(nombre)

"""condicionales"""

edad = 15

def verificar_si_puede_conducir(edad):
  if edad >= 18:
    print("usted tiene edad suficiente para conducir")
  else:
    print ("usted no tiene edad para conducir")

verificar_si_puede_conducir(edad)

"""conversion de tipos de datos"""

def verificar_si_puede_conducir_sin_parametro():
  edad = input('digite su edad: ')
  edad = int(edad)
  if edad >= 18:
    print("usted tiene edad suficiente para conducir")
  else:
    print ("usted no tiene edad para conducir")


verificar_si_puede_conducir_sin_parametro()

"""CREANDO LISTAS"""

edades = [18,15,12,45,50]

edades

type(edad)

type(nombre)

type(edades)

edades

edades[2]

#[18,15,12,45,50]
#  0  1  2 3  4
edades[1]

edades[0:2]

edades[0:3]

edades[:]

edades[1:]

#python nos permite poner indices negativos
#[18, 15, 12, 45, 50]
#     -4   -3 -2  -1
edades[-1]

edades[-3]

"""BUCLES Y CICLOS(CICLOS LOOP)

"""

edades = [18,15,12,45,50]

def verificar_si_puede_conducir(edad):
  if edad >= 18:
    print("usted tiene edad suficiente para conducir")
  else:
    print ("usted no tiene edad para conducir")


for  edad in  edades:
  verificar_si_puede_conducir(edad)

edades = [18,15,12,45,50]

def verificar_si_puede_conducir_con_bucle(edades):
  for  edad in  edades:
   if edad >= 18:
    print("usted tiene edad suficiente para conducir")
  else:
    print ("usted no tiene edad para conducir")


verificar_si_puede_conducir_con_bucle(edades)

"""tipo de dato bolean"""

edad = 18

edad >= 18

edad < 18

edad == 18

verificaciones = []
edades = [13,15,20]
def verificar_si_puede_conducir_bool(verficaciones,edades):
  for edad in edades:
    if edad >= 18:
      verificaciones.append(True)
    else:
        verificaciones.append(False)
  for verificacion in verificaciones:
    if verificacion == True:
      print("usted tiene edad suficiente para conducir")
    else:
      print("usted no tiene edad suficiente para conducir")


verificar_si_puede_conducir_bool(verificaciones,edades)

"""diferentes tipos de listas"""

persona = ["Mariana",25,True,"Mexico"]

persona

for elemento in persona:
  print(f"el elemento {elemento} de la lista es del tipo ",type(elemento))

"""importando librerias"""

from random import randrange,seed

randrange(0,11)

notas_matematicas = []

notas_matematicas.append(randrange(0,11))

notas_matematicas

notas_matematicas = []
seed(8)
for notas in range(6):
  notas_matematicas.append(randrange(0,11))

notas_matematicas

len(notas_matematicas)

"""#biblioteca matplolib para graficos"""

import matplotlib.pyplot as plt

list(range(1,7))

x = list(range(1,7))
y = notas_matematicas

plt.plot(x,y,marker = "o")
plt.title("graficos de las notas de matematicas")
plt.xlabel("pruebas")
plt.ylabel("notas")
plt.show()