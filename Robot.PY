#parancs = 'EEEKDKEKDKEKDDNN'
parancs = input('Kerem a robot parancsait: ')
E = 0
D = 0
K = 0
N = 0

for i in range(0, len(parancs)):
    if parancs[i] == 'E':
        E += 1
    elif parancs[i] == 'D':
        D += 1
    elif parancs[i] == 'K':
        K += 1
    elif parancs[i] == 'N':
        N += 1
    
print('E betuk szama: ', E)
print('D betuk szama: ', D)
print('K betuk szama: ', K)
print('N betuk szama: ', N)

if E > D:
    E -= D
    D = 0
else:
    D -= E
    E = 0

if K > N:
    K -= N
    N = 0
else:
    N -= K
    K = 0

for i in range(E):
    print('E', end='')
for i in range((D)):
    print('D', end='')
for i in range((K)):
    print('K', end='')
for i in range((N)):
    print('N', end='')
