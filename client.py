import socket
import threading
import pickle

def printHeroes(heroes):
    print('**********')
    print('Имя: ' + heroes.name)
    print('Уровень: ' + str(heroes.level))
    print('Сила: ' + str(heroes.dam))
    print('Защита: ' + str(heroes.deff))
    print('За пазухой: ' + str(heroes.item))

def marshrut(napravlenie):
    if napravlenie[0].lower() == 'name':
        printHeroes()
        return level

def read_sok():
    while 1:
        data = sor.recv(1024)
        mass = pickle.loads(data)

        printHeroes(mass[1])

server = "localhost", 5050  # Данные сервера
alias = input('Введите имя: ') # Вводим наш псевдоним
messeg = ['name', alias]
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0)) # Задаем сокет как клиент
sor.sendto(pickle.dumps(messeg), server)# Уведомляем сервер о подключении
potok = threading.Thread(target= read_sok)
potok.start()
while 1:
    mensahe = input()
    # sor.sendto(('['+alias+']'+mensahe).encode('utf-8'), server)
    sor.sendto(pickle.dumps(['open', mensahe]), server)