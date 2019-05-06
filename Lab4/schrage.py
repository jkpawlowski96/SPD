import numpy as np


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

    S = np.zeros(len(jobs_list))  # momenty rozpoczęcia wykonywania zadań
    C = np.zeros(len(jobs_list))  # momenty zakończenia wykonywania zadań

    Nn = list(range(len(jobs_list)))
    Ng = []

    order = []

    # Algorymt
    t = min(R)
    while len(Nn) > 0 or len(Ng) > 0:
        while len(Nn) > 0 and min(R) <= t:
            j = arg_r(min(R), Nn)[0]
            R.remove(min(R))
            Nn.remove(j)
            Ng.append(j)
            Q.append(jobs_list[j].tail[0])
        if len(Ng) == 0:
            t = min(R)
        else:
            j = arg_q(max(Q), Ng)[0]
            Q.remove(max(Q))
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



def schrange_zly(jobs_list):
    '''
    Simulate RPQ problem
    :param jobs_list:
    :param order:
    :return:
    '''

    R = []
    for job in jobs_list:
        R.append(job.head[0])

    S = np.zeros(len(jobs_list))  # momenty rozpoczęcia wykonywania zadań
    C = np.zeros(len(jobs_list))  # momenty zakończenia wykonywania zadań

    Nn = list(range(len(jobs_list)))
    Ng = []

    order = []

    # Algorymt
    t = min(R)
    while len(Nn) > 0 or len(Ng) > 0:

        for i in Nn.copy():
            if jobs_list[i].head[0] <= t:
                Ng.append(i)
                Nn.remove(i)

        if len(Ng) == 0:
            t = min(R)

        # Znaleziono zadania o takim czasie
        if len(Ng) > 0:

            # Tylko jedno zadanie
            if len(Ng) == 1:
                i = Ng.pop()
                order.append(i)
                R.remove(jobs_list[i].head[0])

            # Wiecej niż jedno zadanie
            else:
                Q = []
                for i in Ng:
                    Q.append(jobs_list[i].tail[0])

                # Wybór po najdłuższym czasie dostawy
                max_q = max(Q)
                for i in Ng:
                    if jobs_list[i].tail[0] == max_q:
                        Ng.remove(i)
                        order.append(i)
                        R.remove(jobs_list[i].head[0])
                        t = t + jobs_list[i].body[0]
                        break

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
