import random
class Hero(object):
    def __init__(self, level, dam, deff, item):
        self.level = level
        self.dam = dam
        self.deff = deff
        self.item = item
        self.xy = self.coordinat()

    def levelheroes(self):
        return [self.level, self.dam, self.deff, self.item]

    def coordinat(self):
        # coord = {'x': random.randint(0, 9), 'y': random.randint(0, 9)}
        coord = {'x': random.randint(0, 25)}
        return coord

def Move(moveNext, cikl):
    if moveNext == 'открыть дверь':
        vozmHod(cikl)
        cikl = hod(cikl)

        # level1()
    elif moveNext == 'герой':
        Heroes()
    else:
        return
    return cikl

def vozmHod(Position):
    pyt = ''
    if Position % 5 != 0:
        pyt = pyt + "Влево "
        # print("Влево")
    if (Position + 1) % 5 != 0:
        pyt = pyt + "Вправо "
        # print("Вправо")
    if Position not in range(20, 25):
        pyt = pyt + "Вниз "
        # print("Вниз")
    if Position not in range(0, 5):
        pyt = pyt + "Вверх "
        # print("Вверх")

    print(pyt)

def hod(cikl):
    i = input().lower()
    if i == "вверх":
        cikl = cikl - 5
    elif i == "вниз":
        cikl = cikl + 5
    elif i == "влево":
        cikl = cikl - 1
    elif i == "вправо":
        cikl = cikl + 1
    else:
        print("Ой, туда я не хочу идти")

    return cikl

# x = Hero(1,2,3,4)
# print(x.xy['x'])
# rez = Move(str(input()), x.xy['x'])
# x.xy['x'] = rez
# print(rez)
# print(x.xy['x'])