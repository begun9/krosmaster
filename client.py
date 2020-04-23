import socket
import threading
import pickle, time

hero = ''
def printHeroes(heroes):
    print('**********')
    print('Имя: ' + heroes.name)
    print('Уровень: ' + str(heroes.level))
    print('Сила: ' + str(heroes.dam))
    print('Защита: ' + str(heroes.deff))
    print('За пазухой: ' + str(heroes.item))
    print('**********')

def slovar(fraza):
    nabor = {
        'открыть дверь': 'open',
        'герой': 'heroes'
    }
    return nabor[fraza]


def marshrut(napravlenie):

    if napravlenie[0] == 'name':
        global hero
        hero = napravlenie[1]
        printHeroes(napravlenie[1])
    elif napravlenie[0] == 'open':
        print(napravlenie[1])
    elif napravlenie[0 == 'heroes']:
        printHeroes(napravlenie[1])


def read_sok():
    while 1:
        data = sor.recv(1024)
        mass = pickle.loads(data)
        marshrut(mass)

        # printHeroes(mass[1])

server = "localhost", 5050  # Данные сервера
alias = input('Введите имя: ') # Вводим наш псевдоним
messeg = ['name', alias]
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0)) # Задаем сокет как клиент
sor.sendto(pickle.dumps(messeg), server)# Уведомляем сервер о подключении
potok = threading.Thread(target=read_sok)
potok.start()


while 1:
    time.sleep(0.3)
    mensahe = input('Что делаем? -')

    # sor.sendto(('['+alias+']'+mensahe).encode('utf-8'), server)
    sor.sendto(pickle.dumps([slovar(mensahe.lower()), mensahe, hero.name]), server)