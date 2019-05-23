from job import *
from schrage import *


def carlier_algorithm(jobs_list, UB):
    R = [j.head[0] for j in jobs_list]
    P = [j.body[0] for j in jobs_list]
    Q = [j.tail[0] for j in jobs_list]

    pi, U = schrange_nlogn(jobs_list.copy())
    pi_prim=[]

    if U < UB:
        UB = U
        pi_prim = pi.copy()

    S, C, cmax_pi =calc_s_c(pi, jobs_list.copy())

    #wyznaczenie b
    b=[]
    J = list(range(1, len(pi)))
    for j in J:
        if cmax_pi == (C[j] + Q[j]):
            b.append(j)
    b = max(b)

    #wyznaczenie a
    a =[]
    for j in J:
        sum_jb = sum([P[s] for s in range(j, b+1)]) +Q[b]
        if cmax_pi == (R[j] + sum_jb ):
            a.append(j)
    a = min(a)

    #wyznaczenie c
    c = []
    J = list(range(a, b))
    for j in J:
        if Q[j] == Q[b]:
            c.append(j)

    # jesli nie znaleziono c
    if len(c)==0:
        return pi_prim

    c = max(c)


    #wyznaczenie bloku
    Kappa=[]
    for i in range(c+1, b+1):
        Kappa.append(i)


    r_list=[]
    p_list=[]
    q_list=[]
    for kappa in Kappa:
        r_list.append(jobs_list[pi[kappa]].head[0])
        p_list.append(jobs_list[pi[kappa]].body[0])
        q_list.append(jobs_list[pi[kappa]].tail[0])

    r_Kappa=min(r_list)
    q_Kappa=min(q_list)
    p_Kappa=sum(p_list)

    h_Kappa=r_Kappa+p_Kappa+q_Kappa
        #Kappa u {c}
    r_Kappa_u=min(r_Kappa, jobs_list[c].head[0])
    q_Kappa_u=min(q_Kappa, jobs_list[c].tail[0])
    p_Kappa_u=p_Kappa+jobs_list[c].body[0]
    
    h_Kappa_u=r_Kappa_u+p_Kappa_u+q_Kappa_u


    #lewy potomek - zmiana wartosci r zadania krytycznego
    old_rc=jobs_list[c].head[0]
    jobs_list[c].head[0]=max(jobs_list[c].head[0], r_Kappa+p_Kappa)

    LB=schargepmtn_nlogn(jobs_list)
    LB=max(h_Kappa, h_Kappa_u, LB)
    
    if LB<UB: #jesli jest sens...
        pi_prim = carlier_algorithm(jobs_list, UB)

    #powrot z wartoscia r
    jobs_list[c].head[0]=old_rc

    #prawy potomek - zmiana wartosci q zadania krytycznego
    old_qc=jobs_list[c].tail[0]
    jobs_list[c].tail[0]=max(jobs_list[c].tail[0], q_Kappa+p_Kappa)
    
    LB=schargepmtn_nlogn(jobs_list)
    LB=max(h_Kappa, h_Kappa_u, LB)

    if LB<UB: #jesli jest sens...
        pi_prim = carlier_algorithm(jobs_list, UB)

    #powrot z wartoscia q
    jobs_list[c].tail[0]=old_qc
    return pi_prim

    
def cmax_tab(jobs_list, order):
    cmax_tab=[]
    c=0
    for num in order:        
        if jobs_list[num].head[0]>c:
            cmax_tab.append(jobs_list[num].head[0]+jobs_list[num].body[0])
            c=jobs_list[num].head[0]+jobs_list[num].body[0]
        else:
            c=c+jobs_list[num].body[0]
            cmax_tab.append(c)
    return cmax_tab





