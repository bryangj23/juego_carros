"""
● Configurar Juego: Crear juego con jugadores, el juego debe tener los limites de
kilómetros por cada pista (un jugador puede ser un conductor y un conductor debe
tener un carro asociado y un carro debe estar asociado a un carril que a su vez debe
estar en una pista)
"""
from jugadores import Jugador
from carros import Carro
from random import randint
import csv

pistas={1:{'kilometros':1,'cariles':3},2:{'kilometros':3,'cariles':3},3:{'kilometros':30,'cariles':3}}
juego=[]
opcion=0
pista=[]
jugadores=[]
i=1

print("*********************************** Carros ************************************\n")
print("Nuevo juego...")
print('\n*Para iniciar el juego elija la pista (numero) en la que desea jugar:')
print('Para iniciar el juego, elija la pista (numero) en la que desea jugar:\nPistas:')

#    Mostrando pistas
for g in pistas:
    print(f" {g}: Kilometros: {pistas.get(g)['kilometros']}, numeros de cariles: {pistas.get(g)['cariles']} ")

opcion=int(input('Ingrese el (numero) de la pista: '))

pista=[pistas[opcion]['kilometros'],pistas[opcion]['cariles']]

print("\n***************  Para iniciar el juego debe crear los 3 jugadores *************")
while i <= pista[1]:

    nombre=input(f"\nIngrese el nombre del jugador{i}:")
    jugadores.append(Jugador(nombre))
    i+=1

for c in range(pista[1]):
    juego.append(Carro(jugadores[c]))

termino=-True
while termino:

    print('\n**** AVANCE *****')
    for i in juego:

        i.set_pos(i.get_pos()+randint(1,6)*100)
        print(i.getKm())

        if (i.getKm()) >= pista[0]:
            termino=False
            break

#Ordenando segun llegada
podio= sorted(juego, key=lambda objeto: objeto.posicion, reverse=True)

#Mostrando ganadores
print(f"\nEn el primer lugar: {podio[0].jugador.getNombre()}, {podio[0].get_pos()}m, {podio[0].getKm()}km")
print(f"En el segundo lugar: {podio[1].jugador.getNombre()}, {podio[1].get_pos()}m, {podio[1].getKm()}km")
print(f"En el tercer lugar: {podio[2].jugador.getNombre()}, {podio[2].get_pos()}m, {podio[2].getKm()}km")

guardar=(f"\nEn la pista {opcion}; 1; {podio[0].jugador.getNombre()}; {podio[0].get_pos()}m; 2; {podio[1].jugador.getNombre()}, {podio[1].get_pos()}m; 3; {podio[2].jugador.getNombre()}; {podio[2].get_pos()}m")


with open('juega.csv','a') as fd:
    fd.write(guardar)
