"""generowanie statkow do pliku"""

import random

lista_statkow = []

for i in range(200):
    temp_id_ship = ""
    if i < 10:
        temp_id_ship = "S00"+str(i)
    elif i < 100:
        temp_id_ship = "S0"+str(i)
    else:
        temp_id_ship = "S"+str(i)

    #generowanie wymiarow dla statku

    w = random.randrange(50, 101)
    l = random.randrange(50, 101)
    h = random.randrange(50, 101)

    statek = {
        "id_ship": temp_id_ship,
        "width_ship": w,
        "height_ship": h,
        "length_ship": l,
    }

    lista_statkow.append(statek)


print(lista_statkow)

plik = open("statki.txt", 'w')
try:
    #plik.writelines(str(lista_statkow))

    for i in lista_statkow:
        plik.writelines(str(i) + '\n')



finally:
    plik.close()


"""generowanie kontenerow do pliku"""


lista_kontenerow = []

#generowanie wysokosci dla kontenerow
h = random.randrange(1, 41)

for i in range(1000):
    temp_id_container = ""
    if i < 10:
        temp_id_container = "C00"+str(i)
    elif i < 100:
        temp_id_container = "C0"+str(i)
    else:
        temp_id_container = "C"+str(i)

    #generowanie wymiarow dla kontenerow

    w = random.randrange(1, 41)
    l = random.randrange(1, 41)


    kontener = {
        "id_container": temp_id_container,
        "width_container": w,
        "height_container": h,
        "length_container": l,
    }

    lista_kontenerow.append(kontener)


print(lista_kontenerow)

plik = open("kontenery.txt", 'w')
try:
    #plik.write(str(lista_kontenerow) + '\n')
    for i in lista_kontenerow:
        plik.writelines(str(i) + '\n')
finally:
    plik.close()