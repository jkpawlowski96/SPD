import numpy as np

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

#Johnson's rule (two machines)
def AlgJohn2(jobs):
    #group 1 contains jobs which time(0)<time(1)
    #group 2 contains other jobs
    G1=[]
    G2=[]
    for i in range(len(jobs)):
        if jobs[i].time(0)<jobs[i].time(1):
            G1.append([i, jobs[i].time(0), jobs[i].time(1)])
            print("G1: %d"%i)
        else:
            G2.append([i, jobs[i].time(0), jobs[i].time(1)])
            print("G2: %d"%i)

    #if len(G1):
    #    G1[0].sort_asc(0) #sort by time on machine 0 (asc)
    #if len(G2):
    #    G2[0].sort_desc(1) #sort by time on machine 1 (desc)

    G=G1+G2
    ind=[]
    #optimal order
    for i in range(len(G)):
        ind.append(G[i][0])
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
        for i in range(len(jobs)):
            for j in range(len(jobs)-1):
                #times on virtual machines
                times.append(jobs[i].time(j)+jobs[i].time(j+1))
            virtual_jobs_list.append(Job(times))
            times=[]
        return AlgJohn(virtual_jobs_list)