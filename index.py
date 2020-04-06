import socket
import persone
import pickle, random

class Heroes(object):
    def __init__(self, level, dam, deff, item):
        self.level = level
        self.dam = dam
        self.deff = deff
        self.item = item
        self.xy = self.coordinat()

    def levelheroes(self):
        return [self.level, self.dam, self.deff, self.item]

    def coordinat(self):
        coord = {'x': random.randint(0, 9), 'y': random.randint(0, 9)}
        return coord


def Map():
    x = 0
    OsX = []
    while x<=10:
        OsX.append(x)
        x += 1
    return OsX

Maps = Map()
print(Maps)

level = Heroes(1, 4, 5, 0)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


sock.bind(('localhost', 5050))
client = [] # Массив где храним адреса клиентов
print('Start Server')
while 1:
    data, addres = sock.recvfrom(1024)
    print(addres[0], addres[1])
    if addres not in client:
        client.append(addres) # Если такова клиента нету , то добавить
    for clients in client:
        # if clients == addres:
        #     continue # Не отправлять данные клиенту который их прислал
        sock.sendto(pickle.dumps(level.levelheroes()), clients)