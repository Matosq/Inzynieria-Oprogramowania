import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from resources import *
from scheduler import *

"""
Głowny plik dla algorytmu pierwszego - algorytm wlasnego pomyslu (zachlanny)
"""

scheduler = Resources()

scheduler.getActiveContainers()


index_of_report = 0

"""
Glowna petla programu. Tworzymy 5 raportow.
W kazdej iteracji wybieramy jeden z trzech statkow dla ktorego udalo sie zaladowac najwiecej kontenerow. 
Nastepnie statek jest wysylany tzn tworzony jest dla niego raport. Wybrany statek i kontenery sa usuwane z listy.    
"""
for j in range(5):
    index_of_optimal = 0

    optimal = 0
    for ship, index_of_ship in zip(scheduler.active_ships, range(3)):
        temp = allocation(scheduler, ship)

        if temp > optimal:
            optimal = temp
            index_of_optimal = index_of_ship

    print("Indeks najlepszego: ", index_of_optimal)

    loaded_containers = create_report(scheduler, scheduler.active_ships[index_of_optimal], index_of_report)
    index_of_report += 1

    "Usuwamy z listy aktywnych kontenerow zaladowane kontenery"
    for i in loaded_containers:
        scheduler.active_containers.remove(i)

    "Usuwamy statek z listy aktywnych statkow"
    scheduler.active_ships.pop(index_of_optimal)
    scheduler.setActiveShips()

scheduler.getActiveShips()
print("KONIEC PROGRAMU algorytm 1")