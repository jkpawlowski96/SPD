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

