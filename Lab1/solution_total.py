from itertools import *
from algorithms import *
import time as t

clock=0#clock

def mtime(opt='start'):
    global clock

    if opt == 'start':
        #clock=time.time()
        clock =t.time()

    if opt =='stop':
        clock = t.time()-clock
        print('Measured time:',clock,'s')
        return clock


#Load jobs from file
jobs_list=jobs_load('./ta000.txt')

#List of jobs_index
jobs_queue = range(np.shape(jobs_list)[0])  # [0, 1, 2, n]

#Total permutation of jobs
jobs_perm = list(permutations(jobs_queue)) # [[1,2,3],[2,3,1]...]


"""
1) Total overview
"""
Tmin=0
for comb in jobs_perm:    # for all combinations
    if Tmin==0:
        Tmin=c_max(comb, jobs_list)
        order_total=comb
    else:
        time=c_max(comb, jobs_list)
        if Tmin > time:
            Tmin=time
            order_total=comb
    #print('Time of comb sim_ ', i, ':', sim_time_queue(comb, jobs_list))      #time of combination
    #print('Time of comb cmax ', i, ':', cmax(comb, jobs_list))      #time of combination

mtime()
c_max(order_total,jobs_list)
t=mtime('stop')

print('cmax perm time: ',Tmin, '   order: ', order_total)

"""
2)Johnson algorithm
"""
order=AlgJohn(jobs_list)
print('Alg John, time: ',c_max(order_total, jobs_list), '   order: ', order_total)
