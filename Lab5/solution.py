from job import *
from schrage import *
from carlier import *

jobs_list = jobs_load('./dane_testowe_RPQ/in50.txt')
order0 = range(len(jobs_list))
order, cmax = carlier_algorithm(jobs_list)
print('in50.txt',cmax)

jobs_list = jobs_load('./dane_testowe_RPQ/in100.txt')
order0 = range(len(jobs_list))
order, cmax = carlier_algorithm(jobs_list)
print('in100.txt',cmax)

jobs_list = jobs_load('./dane_testowe_RPQ/in200.txt')
order0 = range(len(jobs_list))
order, cmax = carlier_algorithm(jobs_list)
print('in200.txt',cmax)

