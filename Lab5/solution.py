from job import *
from schrage import *
from carlier import *

'''
nazwa='./dane_testowe_RPQ/ola2.txt.'
data='ola2.txt'
print(data)
jobs_list = jobs_load2(nazwa)
pi, U = schrange(jobs_list)
print('Schrage ', U)
U= schargepmtn(jobs_list)
print('Schrage pmtn ', U, '\n')
order, UB = carlier_algorithm(jobs_list, 100000000)
print('UB=', UB)
print(order)
print(pi)
tab=cmax_tab(jobs_list, order)
tab_end=[]
for j in range(len(tab)):
    tab_end.append(tab[j]+jobs_list[order[j]].tail[0])
data='ola.txt'
if len(tab_end)>0:
    print(data,max(tab_end), '   --->   ')

print('\n ----------------------------')
'''
nazwa='./dane_testowe_RPQ/ola.txt.'
data='ola.txt'
print(data, 'prawidlowe wartosci dla pierwszego wezla (a,b)=(4, 12), c=1',)
jobs_list = jobs_load2(nazwa)
pi, U = schrange(jobs_list)
print('Schrage ', U)
U= schargepmtn(jobs_list)
print('Schrage pmtn ', U, '\n')
order, UB = carlier_algorithm(jobs_list, 100000000)
print('UB=', UB)
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
wynik=[228, 3026, 3665, 3309, 3191, 3618, 3446, 3821, 3634]
ok=0;
for n in range(9):
    nazwa='./dane_testowe_RPQ/data00'+str(n)+'.txt.'
    jobs_list = jobs_load2(nazwa)
    osch, csch=schrange(jobs_list)
    #print(osch, csch)
    order, UB = carlier_algorithm(jobs_list, 100000)

    data='data00'+str(n)+'.txt'
    if UB==wynik[n]:
        ok+=1
        stat='OK'
    else:
        stat=''

    print(data,UB, '   --->   ', wynik[n], '   ',stat)


jobs_list = jobs_load('./dane_testowe_RPQ/in50.txt')
order, UB = carlier_algorithm(jobs_list, 100000)

if UB==1492:
    ok+=1
    stat='OK'
else:
    stat=''
print('in50.txt',UB, '   --->   ', 1492, '   ',stat)

jobs_list = jobs_load('./dane_testowe_RPQ/in100.txt')
order,UB = carlier_algorithm(jobs_list, 100000)

if UB==3070:
    ok+=1
    stat='OK'
else:
    stat=''
print('in100.txt',UB, '   --->   ', 3070, '   ',stat)

jobs_list = jobs_load('./dane_testowe_RPQ/in200.txt')
order,UB = carlier_algorithm(jobs_list, 100000)

if UB==6398:
    ok+=1
    stat='OK'
else:
    stat=''
print('in200.txt',UB, '   --->   ', 6398, '   ',stat)

print('\n Ilosc poprawnych: ', ok)

'''
