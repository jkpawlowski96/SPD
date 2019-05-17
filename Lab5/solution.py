from job import *
from schrage import *
from carlier import *

wynik=[228, 3026, 3665, 3309, 3191, 3618, 3446, 3821, 3634]
for n in range(9):
    nazwa='./dane_testowe_RPQ/data00'+str(n)+'.txt.'
    jobs_list = jobs_load2(nazwa)
    order = carlier_algorithm(jobs_list, 100000)

    tab=cmax_tab(jobs_list, order)
    tab_end=[]
    for j in range(len(tab)):
        tab_end.append(tab[j]+jobs_list[order[j]].tail[0])
    data='data00'+str(n)+'.txt'
    print(data,max(tab_end), '   --->   ', wynik[n])


jobs_list = jobs_load('./dane_testowe_RPQ/in50.txt')
order = carlier_algorithm(jobs_list, 100000)

tab=cmax_tab(jobs_list, order)
tab_end=[]
for j in range(len(tab)):
    tab_end.append(tab[j]+jobs_list[order[j]].tail[0])
print('in50.txt',max(tab_end), '   --->   ', 1492)

jobs_list = jobs_load('./dane_testowe_RPQ/in100.txt')
order = carlier_algorithm(jobs_list, 100000)

tab=cmax_tab(jobs_list, order)
tab_end=[]
for j in range(len(tab)):
    tab_end.append(tab[j]+jobs_list[order[j]].tail[0])
print('in100.txt',max(tab_end), '   --->   ', 3070)

jobs_list = jobs_load('./dane_testowe_RPQ/in200.txt')
order = carlier_algorithm(jobs_list, 100000)

tab=cmax_tab(jobs_list, order)
tab_end=[]
for j in range(len(tab)):
    tab_end.append(tab[j]+jobs_list[order[j]].tail[0])
print('in200.txt',max(tab_end), '   --->   ', 6398)




