import socket
# import persone
import pickle, random
import heroes

def Move(moveNext, cikl, sock, clients):

    if moveNext == 'открыть дверь':
        print(moveNext)
        sock.sendto(pickle.dumps(vozmHod(cikl)), clients)
        cikl = hod(cikl)
    elif moveNext == 'герой':
        Heroes()
    else:
        sock.sendto(pickle.dumps(vozmHod(cikl)), clients)
        return cikl

    return cikl

def vozmHod(Position):
    pyt = ''
    if Position % 5 != 0:
        pyt = pyt + "Влево "
    if (Position + 1) % 5 != 0:
        pyt = pyt + "Вправо "
    if Position not in range(20, 25):
        pyt = pyt + "Вниз "
    if Position not in range(0, 5):
        pyt = pyt + "Вверх "

    return pyt

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


def Map():
    x = 0
    OsX = []
    while x <= 25:
        OsX.append(x)
        x += 1
    return OsX

Maps = Map()
level = heroes.Hero(1, 4, 5, 0)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('localhost', 5050))
client = [] # Массив где храним адреса клиентов
print('Start Server')
while 1:
    data, addres = sock.recvfrom(1024)
    print(type(data.decode('utf-8')))
    print(addres[0], addres[1])
    print(data.decode('utf-8'))
    otvet = Move(str(data.decode('utf-8')), 1, sock, addres)
    # if addres not in client:
    #     client.append(addres) # Если такова клиента нету , то добавить
    # for clients in client:
    #     break
        # if clients == addres:
        #     continue # Не отправлять данные клиенту который их прислал
        # sock.sendto(pickle.dumps(level), clients)
        # print(otvet)
        # sock.sendto(pickle.dumps(str(otvet)), clients)