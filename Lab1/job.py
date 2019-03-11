import numpy as np
from operator import itemgetter, attrgetter, methodcaller

class Job:
    # Constructor of jobe
    def __init__(self, time_on_machine):
        #array of times per machine
        self.time_on_machine = time_on_machine
        #how many times/machines Job contains
        self.size = np.shape(time_on_machine)[0]

    # Time on machine
    def time(self, machine):
        if machine < self.size:
            #time on specyfic machine
            return self.time_on_machine[machine]
        else:
            #time out of range
            print('Job time() size error')
            return None


def cmax(perm, jobs):
    # array of end times (i-1 job on j-1 machine), now filled with 0
    C = [[0] * (len(perm) + 2) for i in range(jobs[0].size + 2)]

    for j in range(1, jobs[0].size + 1):  # machine number
        for i in range(1, len(perm) + 1):  # job number
            C[j][i] = max(C[j][i - 1], C[j - 1][i]) + jobs[perm[i - 1]].time(j - 1)
    # end time (max of array C)
    Cmax = 0
    for j in range(jobs[0].size+1):
        for i in range(len(perm)+1):
            Cmax = max(Cmax, C[j][i])

    return Cmax


def sim_time_queue(queue, jobs=[Job]):
    machines = np.shape(jobs[0].time_on_machine)[0] # number of machines
    machines_diary = [0] * machines                 # array [t_1,t_2,t_machines] then job is done (new time)
    time=0
    machines_working = [0] * machines

    for job in queue:
        sim_time(jobs[job], machines_diary)

    return machines_diary[machines-1] #the last done job


def sim_time(job, machines_diary):
    machines_list = range(0, np.shape(job.time_on_machine)[0])
    time = 0

    for machine in machines_list:
        delay = machines_diary[machine] - time # job delay
        if delay < 0:
            delay = 0
        time = time + delay + job.time(machine)   # clock time of job done
        machines_diary[machine] = time         # new time in diary


#Johnson's rule (two machines)
def AlgJohn2(jobs):
    #group 1 contains jobs which time(0)<time(1)
    #group 2 contains other jobs
    G1=[]
    G2=[]
    for i in range(len(jobs)):
        if jobs[i].time(0)<jobs[i].time(1):
            G1.append((jobs[i].time(0), jobs[i].time(1), i))
        else:
            G2.append((jobs[i].time(1),jobs[i].time(0), i))

    if len(G1):
        G1.sort()
    if len(G2):
        G2.sort(reverse=True)

    G=G1+G2
    ind=[]
    #optimal order
    for i in range(len(G)):
        ind.append(G[i][2])
    return ind

#Johnson's rule (three machines)
def AlgJohn3(jobs):
    #makes two virtual machines (time on vm0=time(0) + time(1); time on vm1=time(1)+time(2))
    virtual_jobs_list=[]
    for i in range(len(jobs)):
        virtual_jobs_list.append(Job([jobs[i].time(0)+jobs[i].time(1),jobs[i].time(1)+jobs[i].time(2)]))
    return AlgJohn2(virtual_jobs_list)

#Johnson's rule (k machines), I'm not sure if it's correct...
def AlgJohn(jobs):
    if jobs[0].size==2:
        return AlgJohn2(jobs)
    else:
        times=[]
        virtual_jobs_list=[]
        print(jobs[0].size)
        for i in range(jobs[0].size):
            for j in range(len(jobs)):
                #times on virtual machines
                #times.append(jobs[j].time(i)+jobs[j].time(i+1))
                print('.')
            print(times)
            #virtual_jobs_list.append(Job(times))
            times=[]
       # return AlgJohn(virtual_jobs_list)
