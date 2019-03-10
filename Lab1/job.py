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
    C = [[0] * (jobs[0].size + 2) for i in range(len(perm) + 2)]

    for j in range(1, jobs[0].size + 1):  # machine number
        for i in range(1, len(perm) + 1):  # job number
            C[j][i] = max(C[j][i - 1], C[j - 1][i]) + jobs[perm[i - 1]].time(j - 1)

    # end time (max of array C)
    Cmax = 0
    for j in range(len(perm) + 1):
        for i in range(len(perm) + 1):
            Cmax = max(Cmax, C[j][i])

    return Cmax

def AlgJohn(self, jobs):
    #group 1 contains jobs which time(0)<time(1)
    #group 2 contains other jobs
    G1=[]
    G2=[]
    for i in range(len(jobs)):
        if jobs[i].time(0)<jobs[i].time(1):
            G1.append([i, jobs[i].time(0), jobs[i].time(1)])
            print("G1: %d"%i)
        else:
            G1.append([i, jobs[i].time(0), jobs[i].time(1)])
            print("G2: %d"%i)

    if len(G1):
        G1[0].sort(0) #sort by time on machine 0
    if len(G2):
        G2[0].sort(1) #sort by time on machine 1
    G=G1+G2
    ind=[]
    #optimal order
    for i in range(len(G)):
        ind=ind.append(G[i][0])
    return ind