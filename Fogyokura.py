hetek = input('Hetek szama =')
testtömeg = input('Elerni kivant testtomeg (kg) =')
xd = 0
tömeg = []
haha = 0

for i in range(int(hetek)):
    print(i+1,end='')
    tömeg.append(input('. heten='))

for i in range(len(tömeg)):
    if tömeg[i] < testtömeg:
        print('Mari neni a(z) ', i+1 ,' heten erte el a celjat.')
        break
for i in range(len(tömeg)):
    if i > 0 and tömeg[i-1] < tömeg[i]:
        xd += 1
        #print(tömeg[i-1], '->', tömeg[i])
print('A tomege', xd, 'esetben nott egyik hetrol a masikra.')


        