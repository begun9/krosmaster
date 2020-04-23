import socket
# import persone
import pickle, random
import heroes

poolheroes = {}
def Move(moveNext, cikl, sock, clients):

    if moveNext == 'открыть дверь':
        print(moveNext)
        # sock.sendto(pickle.dumps(heroes.vozmHod(cikl)), clients)
        return heroes.vozmHod(cikl)

    elif moveNext == 'герой':
        Heroes()
    else:
        sock.sendto(pickle.dumps(heroes.vozmHod(cikl)), clients)
        return cikl

    return cikl

def Map():
    x = 0
    OsX = []
    while x <= 25:
        OsX.append(x)
        x += 1
    return OsX

def marshrut(napravlenie):
    if napravlenie[0] == 'name':
        level = heroes.Hero(napravlenie[1])
        global poolheroes
        poolheroes.update({level.name: level})
        return ['name', level]
    elif napravlenie[0] == 'open':
        door = Move(napravlenie[1], 1, sock, addres)
        print(door)
        return ['open', door]
    elif napravlenie[0] == 'heroes':
        hero = poolheroes[napravlenie[2]]
        return ['heroes', hero]
    elif napravlenie[0] = 'move':
        move = heroes.hod(napravlenie[1])
        return move


Maps = Map()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('localhost', 5050))
client = [] # Массив где храним адреса клиентов
print('Start Server')
while 1:
    data, addres = sock.recvfrom(1024)
    vhod = pickle.loads(data)
    sock.sendto(pickle.dumps(marshrut(vhod)), addres)



    # otvet = Move(str(pickle.loads(data)[1]), 1, sock, addres)

    # if addres not in client:
    #     client.append(addres) # Если такова клиента нету , то добавить
    # for clients in client:
    #     break
        # if clients == addres:
        #     continue # Не отправлять данные клиенту который их прислал
        # sock.sendto(pickle.dumps(level), clients)
        # print(otvet)
        # sock.sendto(pickle.dumps(str(otvet)), clients)