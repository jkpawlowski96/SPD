import numpy as np
from heap import HeapMax, HeapMin


def max_list(l):
    m = 0
    for v in l:
        if m < v:
            m = v
    return m


def min_list(l):
    m = 99999999999
    for v in l:
        if m > v:
            m = v
    return m


def cmax(jobs_list, C):
    '''
    Last delivered job time
    :param jobs_list:
    :param C:
    :return:
    '''
    max_value = 0
    for job, c in zip(jobs_list, C):
       value = job.tail[0] + c
       if max_value < value:
           max_value = value
    return max_value


def schrange(jobs_list):
    '''
    Simulate RPQ problem
    :param jobs_list:
    :param order:
    :return:
    '''

    def arg_r(v, jobs):
        l = []
        for i in jobs:
            if v == jobs_list[i].head[0]:
                l.append(i)
        return l

    def arg_q(v, jobs):
        l = []
        for i in jobs:
            if v == jobs_list[i].tail[0]:
                l.append(i)
        return l

    R = []
    Q = []
    for job in jobs_list:
        R.append(job.head[0])

    S = np.zeros(len(jobs_list))  # momenty rozpoczęcia wykonywania zadań
    C = np.zeros(len(jobs_list))  # momenty zakończenia wykonywania zadań

    Nn = list(range(len(jobs_list)))
    Ng = []

    order = []

    # Algorymt
    t = min_list(R)
    while len(Nn) > 0 or len(Ng) > 0:
        while len(Nn) > 0 and min_list(R) <= t:
            j = arg_r(min_list(R), Nn)[0]
            R.remove(min_list(R))
            Nn.remove(j)
            Ng.append(j)
            Q.append(jobs_list[j].tail[0])
        if len(Ng) == 0:
            t = min_list(R)
        else:
            j = arg_q(max_list(Q), Ng)[0]
            Q.remove(max_list(Q))
            Ng.remove(j)
            order.append(j)
            t += jobs_list[j].body[0]

    # S czas rozpoczecia zadania
    first = True
    for i in order:
        if first:
            S[i] = jobs_list[i].head[0]
            i_last = i
            first = False
        else:
            S[i] = max(jobs_list[i].head[0], S[i_last]+jobs_list[i_last].body[0])
            i_last = i

    # C czas zakonczenia zadania
    for i in order:
        C[i] = S[i] + jobs_list[i].body[0]

    # Obliczenie cmax
    cmax = []
    for i in order:
        cmax.append(C[i]+jobs_list[i].tail[0])
    # Najdłuższy czas jako ostatnie zakonczone zadania
    cmax = max(cmax)

    return order, cmax


def schrange_nlogn(jobs_list):
    '''
    Simulate RPQ problem
    :param jobs_list:
    :param order:
    :return:
    '''
    def arg_r(v, jobs):
        l = []
        for i in jobs:
            if v == jobs_list[i].head[0]:
                l.append(i)
        return l

    def arg_q(v, jobs):
        l = []
        for i in jobs:
            if v == jobs_list[i].tail[0]:
                l.append(i)
        return l

    R = HeapMin()
    Q = HeapMax()
    for job in jobs_list:
        R.add(job.head[0])

    S = np.zeros(len(jobs_list))  # momenty rozpoczęcia wykonywania zadań
    C = np.zeros(len(jobs_list))  # momenty zakończenia wykonywania zadań

    Nn = list(range(len(jobs_list)))
    Ng = []

    order = []

    # Algorymt
    t = R.min()
    while len(Nn) > 0 or len(Ng) > 0:
        while len(Nn) > 0 and R.min() <= t:
            j = arg_r(R.min(True), Nn)[0]
            Nn.remove(j)
            Ng.append(j)
            Q.add(jobs_list[j].tail[0])
        if len(Ng) == 0:
            t = R.min()
        else:
            j = arg_q(Q.max(True), Ng)[0]
            Ng.remove(j)
            order.append(j)
            t += jobs_list[j].body[0]

    # S czas rozpoczecia zadania
    first = True
    for i in order:
        if first:
            S[i] = jobs_list[i].head[0]
            i_last = i
            first = False
        else:
            S[i] = max(jobs_list[i].head[0], S[i_last]+jobs_list[i_last].body[0])
            i_last = i

    # C czas zakonczenia zadania
    for i in order:
        C[i] = S[i] + jobs_list[i].body[0]

    # Obliczenie cmax
    cmax = []
    for i in order:
        cmax.append(C[i]+jobs_list[i].tail[0])
    # Najdłuższy czas jako ostatnie zakonczone zadania
    cmax = max(cmax)

    return order, cmax


def schargepmtn(jobs_list):

    def arg_r(v,jobs):
        l = []
        for i in jobs:
            if v == jobs_list[i].head[0]:
                l.append(i)
        return l

    def arg_q(v,jobs):
        l = []
        for i in jobs:
            if v == jobs_list[i].tail[0]:
                l.append(i)
        return l

    R = []
    Q = []
    for job in jobs_list:
        R.append(job.head[0])

    #S = np.zeros(len(jobs_list))  # momenty rozpoczęcia wykonywania zadań
    #C = np.zeros(len(jobs_list))  # momenty zakończenia wykonywania zadań

    Nn = list(range(len(jobs_list)))
    Ng = []

    #order = []

    # Algorymt
    t = 0
    l=0
    Cmax=0
    while len(Nn) > 0 or len(Ng) > 0:
        while len(Nn) > 0 and min(R) <= t:
            j = arg_r(min(R), Nn)[0]
            R.remove(min(R))
            Nn.remove(j)
            Ng.append(j)
            Q.append(jobs_list[j].tail[0])
            
            if jobs_list[j].tail[0]>jobs_list[l].tail[0]:
                jobs_list[l].body[0]=t-jobs_list[j].head[0]
                t=jobs_list[j].head[0]

                if jobs_list[l].body[0]>0:
                    Ng.append(l)
                    Q.append(jobs_list[l].tail[0])
                    
        if len(Ng) == 0:
            t = min(R)
        else:
            j = arg_q(max(Q), Ng)[0]
            Q.remove(max(Q))
            Ng.remove(j)
            l=j
            t=t+jobs_list[j].body[0]
            Cmax=max(Cmax, t+jobs_list[j].tail[0])

    return Cmax


def schargepmtn_nlogn(jobs_list):
    def arg_r(v, jobs):
        l = []
        for i in jobs:
            if v == jobs_list[i].head[0]:
                l.append(i)
        return l

    def arg_q(v, jobs):
        l = []
        for i in jobs:
            if v == jobs_list[i].tail[0]:
                l.append(i)
        return l

    R = HeapMin()
    Q = HeapMax()
    for job in jobs_list:
        R.add(job.head[0])

    # S = np.zeros(len(jobs_list))  # momenty rozpoczęcia wykonywania zadań
    # C = np.zeros(len(jobs_list))  # momenty zakończenia wykonywania zadań

    Nn = list(range(len(jobs_list)))
    Ng = []

    # order = []

    # Algorymt
    t = 0
    l = 0
    Cmax = 0
    while len(Nn) > 0 or len(Ng) > 0:
        while len(Nn) > 0 and R.min() <= t:
            j = arg_r(R.min(True), Nn)[0]
            Nn.remove(j)
            Ng.append(j)
            Q.add(jobs_list[j].tail[0])

            if jobs_list[j].tail[0] > jobs_list[l].tail[0]:
                jobs_list[l].body[0] = t - jobs_list[j].head[0]
                t = jobs_list[j].head[0]

                if jobs_list[l].body[0] > 0:
                    Ng.append(l)
                    Q.add(jobs_list[l].tail[0])

        if len(Ng) == 0:
            t = R.min()
        else:
            j = arg_q(Q.max(True), Ng)[0]
            Ng.remove(j)
            l = j
            t = t + jobs_list[j].body[0]
            Cmax = max(Cmax, t + jobs_list[j].tail[0])

    return Cmax
