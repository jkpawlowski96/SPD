from job import *
from itertools import *

jobs_list=[]

# some jobs
jobs_list.append(Job([3, 3, 1]))
jobs_list.append(Job([1 , 4, 2]))
jobs_list.append(Job([1 , 2, 1]))
#jobs_list.append(Job([5 , 1, 9]))


jobs_queue = range(np.shape(jobs_list)[0])  # [0, 1, 2, n]

jobs_perm = list(permutations(jobs_queue)) # [[1,2,3],[2,3,1]...]

print(jobs_perm)
i = 0
for comb in jobs_perm:    # for all combinations
    print('Time of comb ', i, ':', cmax(comb, jobs_list))      #time of combination
    i=i+1


print(AlgJohn(jobs_list))