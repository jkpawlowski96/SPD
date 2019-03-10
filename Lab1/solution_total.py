from job import *
from itertools import *

jobs_list=[]

# some jobs
jobs_list.append(Job([10, 3]))
jobs_list.append(Job([1 , 4]))
jobs_list.append(Job([1 , 1]))

jobs_queue = range(np.shape(jobs_list)[0])  # [0, 1, 2, n]

jobs_perm = list(permutations(jobs_queue)) # [[1,2,3],[2,3,1]...]

print(jobs_perm)
i = 0
for comb in jobs_perm:    # for all combinations
    print('Time of comb ', i, ':', cmax(comb, jobs_list))      #time of combination
    i=i+1

#AlgJohn(jobs_list)