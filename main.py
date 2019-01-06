import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from resources import *
from scheduler import *





scheduler = Resources()


scheduler.getActiveContainers()

for i in scheduler.active_containers:
    print(i)


index_of_report = 0
for j in range(5):
    index_of_optimal = 0

    optimal = 0
    for ship, index_of_ship in zip(scheduler.active_ships, range(3)):
        temp = allocation(scheduler, ship)

        if temp > optimal:
            optimal = temp
            index_of_optimal = index_of_ship

    print("Indeks najlepszego: ", index_of_optimal)

    index_of_report += 1
    loaded_containers = create_report(scheduler, scheduler.active_ships[index_of_optimal], index_of_report)

    "Usuwamy z listy aktywnych kontenerow zaladowane kontenery"
    for i in loaded_containers:
        scheduler.active_containers.remove(i)

    "Usuwamy statek z listy aktywnych statkow"
    scheduler.active_ships.pop(index_of_optimal)
    scheduler.setActiveShips()

    for i in scheduler.active_containers:
        print(i)

scheduler.getActiveShips()
print(scheduler.getActiveContainers())
print("AKTYWNE KONTENERY: ", len(scheduler.active_containers))
