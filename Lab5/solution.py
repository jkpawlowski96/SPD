from job import *
from schrage import *
from carlier import *


jobs_list = jobs_load('./dane_testowe_RPQ/in50.txt')
order = carlier_algorithm(jobs_list, 100000)

tab=cmax_tab(jobs_list, order)
tab_end=[]
for j in range(len(tab)):
    tab_end.append(tab[j]+jobs_list[order[j]].tail[0])
print('in50.txt',max(tab_end))

jobs_list = jobs_load('./dane_testowe_RPQ/in100.txt')
order = carlier_algorithm(jobs_list, 100000)

tab=cmax_tab(jobs_list, order)
tab_end=[]
for j in range(len(tab)):
    tab_end.append(tab[j]+jobs_list[order[j]].tail[0])
print('in100.txt',max(tab_end))

jobs_list = jobs_load('./dane_testowe_RPQ/in200.txt')
order = carlier_algorithm(jobs_list, 100000)

tab=cmax_tab(jobs_list, order)
tab_end=[]
for j in range(len(tab)):
    tab_end.append(tab[j]+jobs_list[order[j]].tail[0])
print('in200.txt',max(tab_end))

