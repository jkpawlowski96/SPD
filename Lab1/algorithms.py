from job import *

def c_max(queue, jobs=[Job]):
    """
    Simulate process
    :param queue: An order to simulate total time
    :param jobs:  list(Job) contains times on machines
    :return: Total Time
    """
    def sim_time(job, machines_diary):
        machines_list = range(0, np.shape(job.time_on_machine)[0])
        time = 0

        for machine in machines_list:
            delay = machines_diary[machine] - time  # job delay
            if delay < 0:
                delay = 0
            time = time + delay + job.time(machine)  # clock time of job done
            machines_diary[machine] = time  # new time in diary

    machines = np.shape(jobs[0].time_on_machine)[0] # number of machines
    machines_diary = [0] * machines                 # array [t_1,t_2,t_machines] then job is done (new time)
    time=0
    machines_working = [0] * machines

    for job in queue:
        sim_time(jobs[job], machines_diary)

    return machines_diary[machines-1] #the last done job


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
        G1.sort() #asc
    if len(G2):
        G2.sort(reverse=True) #desc

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

def AlgJohn(jobs):
    num=num_of_machines(jobs)
    if num == 0:
        return 0
    elif num==2:
        return AlgJohn2(jobs)
    elif num==3:
        return AlgJohn3(jobs)
    else:
        return 0#-1

    '''
    if jobs[0].size==2:
        for i in range(len(jobs)):
            if jobs[i].size==2:
                is_ok=True
            else:
                is_ok=False
        if is_ok:
            return AlgJohn2(jobs)
    elif jobs[0].size==3:
        for i in range(len(jobs)):
            if jobs[i].size==3:
                is_ok=True
            else:
                is_ok=False
        if is_ok:
            return AlgJohn3(jobs)
    else:
        print('Incorrect data!')
'''
#Johnson's rule (k machines)
def AlgJohnk(jobs):
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
