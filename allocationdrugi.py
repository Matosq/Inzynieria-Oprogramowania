from resources import *
from rectpack import newPacker
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def visualisation(sh, conts, levels, h_level):
    """
    Wizualizacja kontenerow na statku
    :param sh: wybrany statek
    :param conts: lista wybranych kontenerow do wizualizacji
    :param levels: liczba pieter na statku
    :param h_level: wysokosc pietra na statku, czyli wysokosc kontenera
    :return: funkcja nic nie zwraca, rysuje wykres
    """
    width_ship = sh['width_ship']
    height_ship = sh['height_ship']
    length_ship = sh['length_ship']

    x, y, z = np.indices((width_ship, length_ship, height_ship))
    "Przygotowanie wykresu"
    voxels = (x == 0) & (y == 0) & (z == 0)
    colors = np.empty(voxels.shape, dtype=object)

    for c in conts:
        b, x_c, y_c, w, h, rid = c
        cube = (x >= x_c) & (x < (x_c + w))
        cube &= (y >= y_c) & (y < (y_c + h))
        cube &= (z >= (b*h_level)) & (z < (b*h_level+h_level))
        random_color = (np.random.rand(1, 3))

        colors[cube] = matplotlib.colors.to_hex(random_color[0], keep_alpha=False)
        voxels |= cube

    "Rysowanie wizualizacji"
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(voxels, facecolors=colors, edgecolor=None)
    plt.show()


def allocation2(index_ship, scheduler, visual=False, number_active_containers=100):
    """
    Funkcja korzysta z modulu rectpack i uklada kontenery na statku. Nie tworzy raportu. Zwraca liczbe zaladowanych kontenerow
    :param index_ship: wybor statku z listy o podanym indeksie
    :param scheduler: obiekt klasy Resources
    :param visual: jesli False wizualizacja nie jest rysowana
    :param number_active_containers: liczba kontenerow ktore zostana zaciagnete z listy, domyslnie 100
    :return: liczba zaladowanych kontenerow na statek
    """
    containers = scheduler.active_containers_2[:number_active_containers]
    ship = scheduler.active_ships[index_ship]
    packer = newPacker()

    "Ustalenie liczby pieter na statku"
    height_of_level = containers[0]['height_container']
    number_of_levels = int(ship['height_ship'] / height_of_level)

    for i in range(1, number_of_levels+1):
        #print("Dodaje poziom nr: ", i)
        packer.add_bin(ship['width_ship'], ship['length_ship'])

    for c in containers:
        packer.add_rect(c['width_container'], c['length_container'], c['id_container'])

    "Pakowanie kontenerow"
    packer.pack()

    #print("liczba kontenerow w rect_list ", len(packer.rect_list()))
    #print(packer.rect_list())

    number_of_containers = 0
    full_ship = False
    for i in range(number_of_levels):
        try:
            #print("Dodaje sume kontenerow z poziomu: ", i," = ", len(packer[i]))
            number_of_containers += len(packer[i])
        except IndexError:
            print("BRAKLO KONTENEROW! Sprobujemy jeszcze raz zaladowac z wiekszą liczbą")
            full_ship = True
            break

    if full_ship is True:
        number_of_containers = allocation2(index_ship, scheduler, visual, number_active_containers+100)

    "Rysowanie wizualizacji"
    if visual is True:
        visualisation(ship, packer.rect_list(), number_of_levels, height_of_level)

    return number_of_containers


def create_report2(index_ship, scheduler, visual=False, number_active_containers=100, number_of_report=0):
    """
    Funkcja laduje kontenery na wybrany statek oraz tworzy raport. Zwraca liste zaladowanych kontenerow
    :param index_ship: indeks na liscie wybranego statku
    :param scheduler: obiekt klasy Resources
    :param visual: jesli False to wizualizacja nie jest rysowana
    :param number_active_containers: liczba kontenerow ktore zostana zaciagniete z listy
    :param number_of_report: indeks kolejnego raportu
    :return: lista zaladowanych kontenerow
    """
    containers = scheduler.active_containers_2[:number_active_containers]
    ship = scheduler.active_ships[index_ship]
    packer = newPacker()

    "Ustalenie wysokosci pietra"
    height_of_level = containers[0]['height_container']
    number_of_levels = int(ship['height_ship'] / height_of_level)

    for i in range(1, number_of_levels+1):
        #print("Dodaje poziom nr: ", i)
        packer.add_bin(ship['width_ship'], ship['length_ship'])

    for c in containers:
        packer.add_rect(c['width_container'], c['length_container'], c['id_container'])

    "Funkcja pakujaca kontenery"
    packer.pack()

    #print("liczba kontenerow w rect_list ", len(packer.rect_list()))
    #print(packer.rect_list())


    number_of_containers = 0
    full_ship = False
    for i in range(number_of_levels):
        try:
            #print("Dodaje sume kontenerow z poziomu: ", i," = ", len(packer[i]))
            number_of_containers += len(packer[i])
        except IndexError:
            print("BRAKLO KONTENEROW! Sprobujemy jeszcze raz zaladowac z wiekszą liczbą")
            full_ship = True
            break

    containers_list = packer.rect_list()
    containers_to_return = []

    if full_ship is True:
        containers_to_return = create_report2(index_ship, scheduler, visual, number_active_containers+100)
    else:
        for c in containers_list:
            b, x_c, y_c, w, h, rid = c
            for i in containers:
                if rid == i['id_container']:
                    containers_to_return.append(i)
                    break

    "Rysowanie wizualizacji"
    if visual is True:
        visualisation(ship, packer.rect_list(), number_of_levels, height_of_level)

    "Raport do pliku"

    plik = open("report_second_algorithm" + str(number_of_report) + ".txt", 'w')
    try:
        plik.writelines(str(ship) + '\n')
        number_of_conts = 0
        for i in containers_to_return:
            plik.writelines(str(i) + '\n')
            number_of_conts += 1
        plik.writelines("Liczba zaladowanych kontenerow: " + str(number_of_conts) + '\n')
    finally:
        plik.close()

    return containers_to_return




