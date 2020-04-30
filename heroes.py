import random
import pickle
class Hero(object):
    def __init__(self, name):
        self.level = 1
        self.dam = random.randint(2, 5)
        self.deff = random.randint(2, 5)
        self.item = 0
        self.name = name
        self.xy = self.coordinat()
        self.position = "start"

    def levelheroes(self):
        return [self.name, self.level, self.dam, self.deff, self.item]

    def coordinat(self):
        # coord = {'x': random.randint(0, 9), 'y': random.randint(0, 9)}
        coord = {'x': random.randint(0, 25)}
        return coord

def Move(moveNext, cikl, sock, clients):
    if moveNext == 'открыть дверь':
        # print(moveNext)
        # sock.sendto(pickle.dumps(vozmHod(cikl)), clients)
        return vozmHod(cikl)

        # cikl = hod(cikl)
    elif moveNext == 'герой':
        Heroes()
    elif moveNext == 'наверх' or moveNext == 'вниз' or moveNext == 'налево' or moveNext == 'направо':
        hod()
    else:
        sock.sendto(pickle.dumps(vozmHod(cikl)), clients)
        return cikl

    return cikl

def vozmHod(Position):
    pyt = ''
    if Position % 5 != 0:
        pyt = pyt + "Налево "
        # print("Влево")
    if (Position + 1) % 5 != 0:
        pyt = pyt + "Направо "
        # print("Вправо")
    if Position not in range(20, 25):
        pyt = pyt + "Вниз "
        # print("Вниз")
    if Position not in range(0, 5):
        pyt = pyt + "Вверх "
        # print("Вверх")

    return pyt

def hod(cikl, move):
    i = move
    ciklDvigenia = cikl.xy['x']
    if i == "вверх":
        cikl.xy['x'] = ciklDvigenia - 5
    elif i == "вниз":
        cikl.xy['x'] = ciklDvigenia + 5
    elif i == "налево":
        cikl.xy['x'] = ciklDvigenia - 1
    elif i == "направо":
        cikl.xy['x'] = ciklDvigenia + 1
    else:
        print("Ой, туда я не хочу идти")

    return cikl