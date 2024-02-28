import random
print("Milyen muveletet szeretne gyakorolni?")
print('\n')
print("1. Osszeadas")
print("2. Kivonas")
print("3. Szorzas")

Valasztas = input("Valasztas (1-3): ")

db = 0
ok = 0
a = 0
b = 0
c = None
d = None


while ok < 5:
    db += 1
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = None
    d = None
    
    if int(Valasztas) == 1:
        print(a, "+", b,end="")
        c = input("= ")
        d = a + b

        
    elif int(Valasztas) == 2:
        c = input( a, "-", b, "= ")
        d = a - b
    elif int(Valasztas) == 3:
        c = input( a, "*", b, "= ")
        d = a * b

    if int(c) == d:
        ok += 1
        print("Helyes")
    else:
        print("Hibás")

Print('Gratulálunk! \n Sikerült', db, 'helyes műveletetelvégezni', ok, 'próbálkozásból.')
