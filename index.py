import socket
import persone
import pickle

class Heroes(object):
    def __init__(self, level, dam, deff, item):
        self.level = level
        self.dam = dam
        self.deff = deff
        self.item = item

    def levelheroes(self):
        return [self.level.encode('utf-8'), self.level.encode('utf-8'), self.level.encode('utf-8')]


level = Heroes('a', 'b', 'c', 'd')


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