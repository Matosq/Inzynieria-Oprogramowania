from resources import *
from rectpack import newPacker
from allocationdrugi import *

"""
Głowny plik dla algorytmu drugiego - wykorzystanie modulu rectpack do ukladania kontenerow
"""

scheduler = Resources()


scheduler.getActiveShips()
index_of_report = 0

"""
Glowna petla programu. Tworzymy 5 raportow.
W kazdej iteracji wybieramy jeden z trzech statkow dla ktorego udalo sie zaladowac najwiecej kontenerow. 
Nastepnie statek jest wysylany tzn tworzony jest dla niego raport. Wybrany statek i kontenery sa usuwane z listy.    
"""
for j in range(5):
    index_of_optimal = 0
    optimal = 0
    for i in range(3):
        temp = (allocation2(i, scheduler, False, 200))
        if temp > optimal:
            optimal = temp
            index_of_optimal = i

    print("Indeks najlepszego statku: ", index_of_optimal, " Załadowalismy ", optimal, " kontenerow")

    loaded_containers = create_report2(index_of_optimal, scheduler, True, 200, index_of_report)
    index_of_report += 1
    "Usuwamy z listy aktywnych kontenerow zaladowane kontenery"
    for i in loaded_containers:
        scheduler.active_containers_2.remove(i)

    "Usuwamy statek z listy aktywnych statkow"
    scheduler.active_ships.pop(index_of_optimal)
    scheduler.setActiveShips()

    scheduler.getActiveShips()

print("KONIEC PROGRAMU algorytm 2")