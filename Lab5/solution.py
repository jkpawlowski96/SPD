from job import *
from schrage import *
from carlier import *
'''
UB=100000000
nazwa='./dane_testowe_RPQ/ola3.txt.'
jobs_list = jobs_load2(nazwa)

order, Cmax = carlier_algorithm(jobs_list,10000000)
#print('wynik Carliera',order,)
#print(order)
print(Cmax)
'''
'''
print('\n ----------------------------')

nazwa='./dane_testowe_RPQ/ola.txt.'
data='ola.txt'
print(data, 'prawidlowe wartosci dla pierwszego wezla (a,b)=(4, 12), c=1',)
jobs_list = jobs_load2(nazwa)
pi, U = schrange(jobs_list)
print('Schrage ', U)
U= schargepmtn(jobs_list)
print('Schrage pmtn ', U, '\n')
order, Cmax = carlier_algorithm(jobs_list, 100000000,0)
print('Cmax=', Cmax)
print(order)
print(pi)
tab=cmax_tab(jobs_list, order)
tab_end=[]
for j in range(len(tab)):
    tab_end.append(tab[j]+jobs_list[order[j]].tail[0])
data='ola.txt'
if len(tab_end)>0:
    print(data,max(tab_end), '   --->   ')

'''
pliki=[0,1,3,4]
wynik=[228, 3026, 3665, 3309, 3191, 3618, 3446, 3821, 3634]
ok=0;
for n in pliki:
    nazwa='./dane_testowe_RPQ/data00'+str(n)+'.txt.'
    jobs_list = jobs_load2(nazwa)
    order, Cmax = carlier_algorithm(jobs_list, 10000000)

    data='data00'+str(n)+'.txt'

    if Cmax==wynik[n]:
        ok+=1
        stat='OK'
    else:
        stat=''

    print(data,Cmax, '   --->   ', wynik[n], '   ',stat)
    
jobs_list = jobs_load('./dane_testowe_RPQ/in50.txt')
order, Cmax = carlier_algorithm(jobs_list, 10000000)

if Cmax==1492:
    ok+=1
    stat='OK'
else:
    stat=''
print('in50.txt',Cmax, '   --->   ', 1492, '   ',stat)

jobs_list = jobs_load('./dane_testowe_RPQ/in100.txt')
order, Cmax = carlier_algorithm(jobs_list, 10000000)

if Cmax==3070:
    ok+=1
    stat='OK'
else:
    stat=''
print('in100.txt',Cmax, '   --->   ', 3070, '   ',stat)

jobs_list = jobs_load('./dane_testowe_RPQ/in200.txt')
order, Cmax = carlier_algorithm(jobs_list, 10000000)

if Cmax==6398:
    ok+=1
    stat='OK'
else:
    stat=''
print('in200.txt',Cmax, '   --->   ', 6398, '   ',stat)

print('\n Ilosc poprawnych: ', ok)


