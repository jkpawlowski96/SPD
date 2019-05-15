from job import *
from schrage import *
from carlier import *


jobs_list = jobs_load('./dane_testowe_RPQ/in50.txt')
order = carlier_algorithm(jobs_list, 100000)

tab=cmax_tab(jobs_list, order)
cmax=tab[len(tab)-1]
print('in50.txt',cmax)

jobs_list = jobs_load('./dane_testowe_RPQ/in100.txt')
order = carlier_algorithm(jobs_list, 100000)

tab=cmax_tab(jobs_list, order)
cmax=tab[len(tab)-1]
print('in100.txt',cmax)

jobs_list = jobs_load('./dane_testowe_RPQ/in200.txt')
order = carlier_algorithm(jobs_list, 100000)

tab=cmax_tab(jobs_list, order)
cmax=tab[len(tab)-1]
print('in200.txt',cmax)
