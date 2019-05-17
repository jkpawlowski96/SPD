import numpy as np
import random
from operator import itemgetter, attrgetter, methodcaller


class Job:
    """
    Jobs req times on every machine so:

    head=[r1,r2,...,rn] for n machines
    body=[p1,p2,...,pn]
    tail=[q1,q2,...,qn]

    """
    # Constructor of jobe
    def __init__(self, times):
        #array of times per machine
        head_list=[]
        body_list=[]
        tail_list=[]
        for i in range(int(len(times)/3)):
            head_list.append(times[3*i])
            body_list.append(times[3*i+1])
            tail_list.append(times[3*i+2])
        self.head = head_list
        self.body = body_list
        self.tail = tail_list
        #how many times/machines Job contains
        self.size = int(np.shape(times)[0]/3)
        
    # Time on machine
    def time(self, machine):
        if machine < self.size:
            #time on specyfic machine
            return [self.head[machine], self.body[machine], self.tail[machine]]
        else:
            #time out of range
            print('Job time() size error')
            return None


def num_of_machines(jobs):
    #returns number of machines, 0 if jobs list is empty and -1 if number of machines is different
    if len(jobs)==0:
        return 0
    else:
        size_list=[]
        for i in range(len(jobs)):
            size_list.append(jobs[i].size)
        if min(size_list)==max(size_list):
            return min(size_list)
        else:
            return -1

def test_jobs(jobs, machines):
    jobs_list=[]
    times=[]
    for i in range(jobs):
        for j in range(3*machines):
            times.append(random.randint(1,30))
        jobs_list.append(Job(times))
        times=[]
    return jobs_list

def jobs_load(file_path='../dane_testowe_RPQ/in50.txt'):
    """
    Load jobs from file.txt in format:
        jobs machines*3
        head_1 body_1 tail_1
        head_2 body_2 tail_2

        head_n body_n tail_n
    :param file_path: path to .txt file
    :return: list(Job)
    """
    with open(file_path, 'r') as f:
        jobs_list=[]
        lines=[]

        #PARAMETERS
        for line in f:
            lines.append(line)
        param=lines.pop(0).strip().split('   ')
        jobs=int(param[0].strip())
        cols=int(param[1].strip())
        del param
        """Load times"""
        for line in lines:
            if 'str' in line:
                break
            line.rstrip().split('   ')
            values = [int(i) for i in line.split()]
            jobs_list.append(Job(values))

    return jobs_list

def jobs_load2(file_path='./dane.txt'):
    """
    Load jobs from file.txt in format:
                    1 2 4
                    4 6 8
                    1 3 4
    :param file_path: path to .txt file
    :return: list(Job)
    """
    with open(file_path, 'r') as f:
        jobs_list=[]
        lines=[]

        '''Load NAME and PARAMETERS'''
        for line in f:
            lines.append(line)
        name=lines.pop(0)
        param=lines.pop(0)

        """Load times"""
        for line in lines:
            if 'str' in line:
                break
            values = [int(i) for i in line.split()]
            jobs_list.append(Job(values))

    return jobs_list

