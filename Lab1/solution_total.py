from job import *
from itertools import *

jobs_list=[]

# some jobs
jobs_list.append(Job([1,1,3]))
jobs_list.append(Job([3,2,1]))
jobs_list.append(Job([1 , 2, 1]))
jobs_list.append(Job([5 , 1, 9]))
jobs_list.append(Job([12 , 2, 1]))
jobs_list.append(Job([1 , 5, 5]))


jobs_queue = range(np.shape(jobs_list)[0])  # [0, 1, 2, n]

jobs_perm = list(permutations(jobs_queue)) # [[1,2,3],[2,3,1]...]

i = 0
for comb in jobs_perm:    # for all combinations
    print('Time of comb ', i, ':', sim_time_queue(comb, jobs_list))      #time of combination
    i=i+1


'''
c=AlgJohn(jobs_list)
print(c)
print('Time of comb ', i, ':', cmax(c, jobs_list))
'''