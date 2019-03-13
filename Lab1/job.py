import numpy as np
from operator import itemgetter, attrgetter, methodcaller


class Job:
    """
    Jobs req times on every machine so:

    time_on_machines=[t1,t2,..,tn] for n machines

    """
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


def jobs_load(file_path='./data.txt'):
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
        for line in f:
            values=line.rstrip().split(' ')
            values=[int(i) for i in values]
            jobs_list.append(Job(values))
            if 'str' in line:
                break
    return jobs_list

