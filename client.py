import socket
import threading
import pickle
def read_sok():
    while 1 :
        data = sor.recv(1024)
        mass = pickle.loads(data)
        print(mass[1])
server = "localhost", 5050  # Данные сервера
alias = input() # Вводим наш псевдоним
sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sor.bind(('', 0)) # Задаем сокет как клиент
sor.sendto((alias+' Connect to server').encode('utf-8'), server)# Уведомляем сервер о подключении
potok = threading.Thread(target= read_sok)
potok.start()
while 1:
    mensahe = input()
    sor.sendto(('['+alias+']'+mensahe).encode('utf-8'), server)