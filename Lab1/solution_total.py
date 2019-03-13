from itertools import *
from algorithms import *

jobs_list=[]


jobs_list=jobs_load()

# some jobs
'''jobs_list.append(Job([5 , 1, 2]))
jobs_list.append(Job([1,1, 1]))
jobs_list.append(Job([3,2, 2]))
jobs_list.append(Job([1 , 2,1]))
jobs_list.append(Job([12 , 2, 1]))
jobs_list.append(Job([1 , 5, 5]))
'''

jobs_queue = range(np.shape(jobs_list)[0])  # [0, 1, 2, n]

jobs_perm = list(permutations(jobs_queue)) # [[1,2,3],[2,3,1]...]

Tmin=0

i = 0
for comb in jobs_perm:    # for all combinations
    if Tmin==0:
        Tmin=c_max(comb, jobs_list)
    else:
        Tmin=min(Tmin, c_max(comb, jobs_list))
    #print('Time of comb sim_ ', i, ':', sim_time_queue(comb, jobs_list))      #time of combination
    #print('Time of comb cmax ', i, ':', cmax(comb, jobs_list))      #time of combination
    i=i+1


print('cmax perm time: ',Tmin)
print('Alg John, time: ',c_max(AlgJohn3(jobs_list), jobs_list))
