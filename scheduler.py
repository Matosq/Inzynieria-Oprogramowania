""" Glowny program, rozwiazanie problemu plecakowego."""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from resources import *


def get_next_container(conts, n, x_thres, y_thres, x_ship, y_ship):
    """
    Funkcja sprawdza czy mozna dopasowac kolejny kontener z listy, jesli sie nie uda zadnego dopasowac zwraca pusty obiekt
    :param conts: lista kontenerow
    :param n:
    :param x_thres: szerokosc do ktorej dopasowac kontener
    :param y_thres: dlugosc do ktorej dopasowac kontener
    :param x_ship: szerokosc statku
    :param y_ship: dlugosc statku
    :return: Kolejny kontener ktory da sie dopasowac lub pusty obiekt
    """
    for next_container in conts:
        if (x_thres + next_container['width_container'] <= x_ship) & (y_thres + next_container['length_container'] <= y_ship):
            return next_container
    return None


def allocation(scheduler, ship):
    """
    Funkcja laduje kontenery na statek. Nie tworzy raportu. Zwraca liczbe zaladowanych kontenerow.
    :param scheduler: obiekt klasy Resources
    :param ship: wybrany statek
    :return: liczba zaladowanych kontenerow
    """
    width_ship = ship['width_ship']
    height_ship = ship['height_ship']
    length_ship = ship['length_ship']

    x, y, z = np.indices((width_ship, length_ship, height_ship))

    containers_1 = scheduler.active_containers[:100]

    "Przygotowanie wykresu"
    voxels = (x == 0) & (y == 0) & (z == 0)
    colors = np.empty(voxels.shape, dtype=object)

    x_threshold = 0
    y_threshold = 0
    z_threshold = 0
    Y_up_threshold = 0

    number_of_containers = len(containers_1)
    height_container = containers_1[0]['height_container']
    number_of_levels = int(height_ship / height_container)
    temp_level = 0
    number = 0

    "Iterujemy, tworzymy poziomy czyli pietra na statku"
    for level in range(number_of_levels):

        for i in range(number_of_containers):
            if len(containers_1) == 0:
                #scheduler.setActiveContainers(100)
                containers_1 = scheduler.active_containers[number:number+100]

            "Wyciagamy nastepny kontener, ktory da sie wlozyc w tym rzedzie"
            container = get_next_container(containers_1, 0, x_threshold, y_threshold, width_ship, length_ship)

            if container is not None:
                #Usuwamy z listy kontenerow wybrany kontener
                containers_1.remove(container)
                number += 1
                #print("Laduje kontener nr ", number, " ", container)
                temp_level = 0

                cube = (x >= x_threshold) & (x < (x_threshold + container['width_container']))
                cube &= (y >= y_threshold) & (y < (y_threshold + container['length_container']))
                cube &= (z >= z_threshold) & (z < (z_threshold + container['height_container']))

                x_threshold += container['width_container']

                if (y_threshold + container['length_container']) > Y_up_threshold:
                    Y_up_threshold = y_threshold + container['length_container']

                "Kolorowanie kontenerow"
                random_color = (np.random.rand(1, 3))

                colors[cube] = matplotlib.colors.to_hex(random_color[0], keep_alpha=False)
                voxels |= cube

            else:
                temp_level += 1
                y_threshold = Y_up_threshold
                x_threshold = 0
                i -= 1

            if temp_level == 3:
                x_threshold = 0
                y_threshold = 0
                z_threshold += height_container
                Y_up_threshold = 0
                break

    "Wizualizacja zapakowanych statkow"

    # fig = plt.figure()
    # ax = fig.gca(projection='3d')
    # ax.voxels(voxels, facecolors=colors, edgecolor=None)
    # plt.show()

    return number


def create_report(scheduler, ship, number_of_report):
    """
    Funkcja laduje kontenery na wybrany statek. Na koncu tworzy raport i zwraca liste zaladowanych kontenerow.
    :param scheduler: obiekt klasy Resources
    :param ship: wybrany statek do zaladwania
    :param number_of_report: ideks do numerowania kolejnych raportow
    :return: lista zaladowanych kontenerow i wpisanych do raportu
    """
    containers_to_report = []
    width_ship = ship['width_ship']
    height_ship = ship['height_ship']
    length_ship = ship['length_ship']

    x, y, z = np.indices((width_ship, length_ship, height_ship))

    #containers_1 = scheduler.active_containers.copy()
    containers_1 = scheduler.active_containers[:100]

    "Przygotowanie wykresu"
    voxels = (x == 0) & (y == 0) & (z == 0)
    colors = np.empty(voxels.shape, dtype=object)

    x_threshold = 0
    y_threshold = 0
    z_threshold = 0
    Y_up_threshold = 0

    number_of_containers = len(containers_1)
    height_container = containers_1[0]['height_container']
    number_of_levels = int(height_ship / height_container)
    temp_level = 0
    number = 0

    "Iterujemy, tworzymy poziomy czyli pietra na statku"
    for level in range(number_of_levels):

        for i in range(number_of_containers):
            if len(containers_1) == 0:
                #scheduler.setActiveContainers(100)
                containers_1 = scheduler.active_containers[number:number+100]

            "Wyciagamy nastepny kontener, ktory da sie wlozyc w tym rzedzie"
            container = get_next_container(containers_1, 0, x_threshold, y_threshold, width_ship, length_ship)

            if container is not None:
                #Usuwamy z listy kontenerow wybrany kontener
                containers_1.remove(container)
                containers_to_report.append(container)
                print("Laduje kontener nr ", number, " ", container)

                number += 1

                temp_level = 0

                cube = (x >= x_threshold) & (x < (x_threshold + container['width_container']))
                cube &= (y >= y_threshold) & (y < (y_threshold + container['length_container']))
                cube &= (z >= z_threshold) & (z < (z_threshold + container['height_container']))

                x_threshold += container['width_container']

                if (y_threshold + container['length_container']) > Y_up_threshold:
                    Y_up_threshold = y_threshold + container['length_container']

                "Kolorowanie kontenerow"
                random_color = (np.random.rand(1, 3))

                colors[cube] = matplotlib.colors.to_hex(random_color[0], keep_alpha=False)
                voxels |= cube

            else:
                temp_level += 1
                y_threshold = Y_up_threshold
                x_threshold = 0
                i -= 1

            if temp_level == 3:
                x_threshold = 0
                y_threshold = 0
                z_threshold += height_container
                Y_up_threshold = 0
                break

    "Raport do pliku"

    plik = open("report"+str(number_of_report)+".txt", 'w')
    try:
        plik.writelines(str(ship) + '\n')
        number_of_conts = 0
        for i in containers_to_report:
            plik.writelines(str(i) + '\n')
            number_of_conts += 1
            #scheduler.active_containers.remove(i)
        plik.writelines("Liczba zaladowanych kontenerow: "+str(number_of_conts) + '\n')
    finally:
        plik.close()

    "Wizualizacja zapakowanych statkow"

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(voxels, facecolors=colors, edgecolor=None)
    plt.show()

    return containers_to_report
