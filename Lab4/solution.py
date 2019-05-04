from job import *
from schrage import *


jobs_list = jobs_load('./dane_testowe_RPQ/in50.txt')
print('Machines:',num_of_machines(jobs_list))
for i in range (len(jobs_list)):
    for j in range (jobs_list[0].size):
        print(jobs_list[i].time(j))

order0 = range(len(jobs_list))
order, cmax = schrange(jobs_list)
print(cmax)
