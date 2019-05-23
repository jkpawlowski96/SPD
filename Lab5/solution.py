from Lab5.job import *
from schrage import *
from carlier import *


nazwa='./dane_testowe_RPQ/ola2.txt.'
jobs_list = jobs_load2(nazwa)
pi, U = schrange_nlogn(jobs_list)
print('Schrage ', U, '\n', pi)
U= schargepmtn_nlogn(jobs_list)
print('Schrage pmtn ', U)
order = carlier_algorithm(jobs_list, 100000)

tab=cmax_tab(jobs_list, order)
tab_end=[]
for j in range(len(tab)):
    tab_end.append(tab[j]+jobs_list[order[j]].tail[0])
data='ola.txt'
if len(tab_end)>0:
    print(data,max(tab_end), '   --->   ')


wynik=[228, 3026, 3665, 3309, 3191, 3618, 3446, 3821, 3634]
ok=0
sum=0
for n in range(9):
    nazwa='./dane_testowe_RPQ/data00'+str(n)+'.txt.'
    jobs_list = jobs_load2(nazwa)
    order = carlier_algorithm(jobs_list, 100000)

    tab=cmax_tab(jobs_list, order)
    tab_end=[]
    for j in range(len(tab)):
        tab_end.append(tab[j]+jobs_list[order[j]].tail[0])
    data='data00'+str(n)+'.txt'
    if len(tab_end)>0:
        print(data,max(tab_end), '   --->   ', wynik[n])
        sum += 1
        if max(tab_end)==wynik[n]:
            ok+=1


jobs_list = jobs_load('./dane_testowe_RPQ/in50.txt')
order = carlier_algorithm(jobs_list, 100000)

tab=cmax_tab(jobs_list, order)
tab_end=[]
for j in range(len(tab)):
    tab_end.append(tab[j]+jobs_list[order[j]].tail[0])
print('in50.txt',max(tab_end), '   --->   ', 1492)
sum += 1
if max(tab_end)==1492:
    ok+=1

jobs_list = jobs_load('./dane_testowe_RPQ/in100.txt')
order = carlier_algorithm(jobs_list, 100000)

tab=cmax_tab(jobs_list, order)
tab_end=[]
for j in range(len(tab)):
    tab_end.append(tab[j]+jobs_list[order[j]].tail[0])
print('in100.txt',max(tab_end), '   --->   ', 3070)
sum += 1
if max(tab_end)==3070:
    ok+=1

jobs_list = jobs_load('./dane_testowe_RPQ/in200.txt')
order = carlier_algorithm(jobs_list, 100000)

tab=cmax_tab(jobs_list, order)
tab_end=[]
for j in range(len(tab)):
    tab_end.append(tab[j]+jobs_list[order[j]].tail[0])
print('in200.txt', max(tab_end), '   --->   ', 6398)
sum += 1
if max(tab_end)==6398:
    ok+=1

print('\n Ilosc poprawnych: ', ok,'na',sum,'->',ok/sum)

