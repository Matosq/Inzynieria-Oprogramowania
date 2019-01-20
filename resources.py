import time


class Resources:
    ships = []
    containers = []

    "Aktywne statki i kontenery w porcie"
    active_ships = []
    active_containers = []

    "Dla drugiego algorytmu"
    active_containers_2 = []

    def __init__(self):
        print("stworzylem obiekt Resources")

    #def getDataFromFile(self):
    #    "Pobranie danych o statkach i kontenerach z plikow"

        plik_statki = open('statki.txt', 'r')

        dict_s = {}

        try:
            for line in plik_statki:
                dict_s = eval(line)
                self.ships.append(dict_s)
        finally:
            plik_statki.close()

        # print(ships)

        plik_kontenery = open('kontenery.txt', 'r')
        dict_c = {}
        try:
            for line in plik_kontenery:
                dict_c = eval(line)
                self.containers.append(dict_c)
        finally:
            plik_kontenery.close()

        # print(containers)

        for x in range(3):
            self.active_ships.append(self.ships[0])
            self.ships.pop(0)

        "Ustalenie Timestampu"
        time_stamp = int(time.time())

        for x in range(1000):
            temp = self.containers[0]
            temp['timestamp'] = time_stamp
            self.active_containers.append(temp)
            self.active_containers_2.append(temp)
            self.containers.pop(0)
            if x % 100 == 0:
                time_stamp += 1111111
        "Sortowanie kontenerow wg najnizszego timestampu, nastepnie wg najwiekszej szerokosci"
        self.active_containers = sorted(self.active_containers, key=lambda k: (k['timestamp'], -k['length_container']))

    def setActiveShips(self):
        "Dobieranie aktywnych stakow. Max 3 na raz w porcie czekajacych na zaladunek"

        self.active_ships.append(self.ships[0])
        self.ships.pop(0)

    def setActiveContainers(self, number=0):
        "Dobieranie aktywnych kontenerow. Max 100 na raz w porcie czekajacych na zaladunek"

        "Ustalenie Timestampu"
        time_stamp = int(time.time())
        for i in range(number):
            temp = self.containers[0]
            temp['timestamp'] = time_stamp
            self.active_containers.append(temp)
            self.containers.pop(0)
        "Sortowanie kontenerow wg najnizszego timestampu, nastepnie wg najwiekszej szerokosci"
        self.active_containers = sorted(self.active_containers, key=lambda k: (k['timestamp'], -k['length_container']))

    def getActiveShips(self):
        print(self.active_ships)

    def getActiveContainers(self):
        return self.active_containers