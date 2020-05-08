import random

def randKub(sumKub):
    kub = []
    for num in range(sumKub):
        kub.append(random.randint(1, 6))
    return kub

def deffKub(deff):
    global rez
    global zash
    if deff[0] == 'з':

        for num in  range(len(deff)-1):
            rez.remove(int(deff[1]))
            zash -=1
    elif deff[0] == 'б':
        global monstor
        global heroes
        for num in range(len(rez)):
            if rez[num] == 6:
                monstor-=2
            elif rez[num] == 5:
                monstor -= 1
            elif rez[num] == 2:
                heroes -=1
            elif rez[num] == 1:
                heroes -= 2

        rez = randKub(heroes)








monstor = 10
heroes = 4
zash = 3

rez = randKub(heroes)
print(rez)

while monstor >= 0:
    deffKub(input().split())
    print(monstor)
    print(heroes)
    print(rez)
    print(zash)
