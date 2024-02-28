import random

n = 10000
dobasok = []
osszeg = 0
Anni = 0
Panni = 0

for i in range(n):
    for i in range(3):
        dobasok.append(random.randrange(1,7))
        osszeg += dobasok[i]

    print('Dobas: ',end='')

    for i in range(len(dobasok)):
        print(dobasok[i],end=' ')

    print("=",osszeg,end='')
    print('       ',end='')

    if osszeg < 10 :
        print('Nyert: Anni')
        Anni += 1
    else:
        print('Nyert: Panni')
        Panni += 1

    dobasok = []
    osszeg = 0
print("A jatek soran " + str(Anni)  + ' alkalommal Anni, ' + str(Panni) + ' alkalommal Panni nyert.')


#write this in c++
# Path: Kozep_szintu_erettsegi_py\kockak.cpp




