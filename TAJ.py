TAJ = '673457015'
ellenorzoszam = TAJ[8]
lst = []
osszeg = 0
print('Az ellenorzo szamjegy: ' + ellenorzoszam)

for i in range(len(TAJ)):
    lst.append(int(TAJ[i:i+1]))

print(lst)

for i in range(len(lst)-1):
    if i % 2 == 1:
        lst[i] *= 3
    if i % 2 == 0:
        lst[i] *= 7

for i in range(len(lst)-1):
    osszeg += lst[i]

print(osszeg%10)
print(TAJ[8])

if osszeg % 10 == int(TAJ[8]):
    print('HELYES')
else:
    print('NEM HELYES')

print(lst)
print(osszeg)

