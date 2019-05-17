from job import *
from schrage import schargepmtn_nlogn, schrange_nlogn
from schrage import cmax

def carlier_algorithm(jobs_list, UB):
    jobs_list = jobs_list.copy()
    pi, U = schrange_nlogn(jobs_list)
    pi_prim = pi[:]

    if U < UB:
        UB = U
        pi_star = pi[:]
    b = -1
    a = -1
    c = -1

    tab=cmax_tab(jobs_list, pi) #tablica zakonczenia wykonywania (r) kolejnych zadan

    #wyznaczenie b
    i=0
    for task in pi:
        if tab[i]+jobs_list[task].tail[0]==U:
            b=task
            ind_b=i
        i=i+1

    #wyznaczenie a    
    i=0
    for task in pi:
        suma=0
        if(i<=ind_b):
            for k in range(i, ind_b+1):
                suma=suma+jobs_list[pi[k]].body[0]
            if jobs_list[task].head[0]+suma+jobs_list[b].tail[0]==U:
                a=task
                ind_a=i
        i=i+1

    #wyznaczenie c
    for i in range(ind_a, ind_b+1):
        if jobs_list[pi[i]].tail[0]<jobs_list[b].tail[0]:
            c=pi[i]
            ind_c=i

    #jesli nie znaleziono c
    if c == -1:
        return pi_star

    #wyznaczenie bloku
    Kappa=[]
    for i in range(ind_c+1, ind_b+1):
        Kappa.append(pi[i])


    r_list=[]
    p_list=[]
    q_list=[]
    for kappa in Kappa:
        r_list.append(jobs_list[kappa].head[0])
        p_list.append(jobs_list[kappa].body[0])
        q_list.append(jobs_list[kappa].tail[0])

    r_Kappa=min(r_list)
    q_Kappa=min(q_list)
    p_Kappa=sum(p_list)

    #lewy potomek - zmiana wartosci r zadania krytycznego
    old_rc=jobs_list[c].head[0]
    jobs_list[c].head[0]=max(jobs_list[c].head[0], r_Kappa+p_Kappa)
    LB=schargepmtn_nlogn(jobs_list)
    
    h_Kappa=r_Kappa+p_Kappa+q_Kappa

    #Kappa u {c}
    r_Kappa_u=min(r_Kappa, jobs_list[c].head[0])
    q_Kappa_u=min(q_Kappa, jobs_list[c].tail[0])
    p_Kappa_u=p_Kappa+jobs_list[c].body[0]
    
    h_Kappa_u=r_Kappa_u+p_Kappa_u+q_Kappa_u
    
    LB=max(h_Kappa, h_Kappa_u, LB)
    
    if LB<UB: #jesli jest sens...
        pi_prim = carlier_algorithm(jobs_list, UB)

    #powrot z wartoscia r
    jobs_list[c].head[0]=old_rc

    #prawy potomek - zmiana wartosci q zadania krytycznego
    old_qc=jobs_list[c].tail[0]
    jobs_list[c].tail[0]=max(jobs_list[c].tail[0], q_Kappa+p_Kappa)
    LB=schargepmtn_nlogn(jobs_list)

    #Kappa u {c}
    r_Kappa_u=min(r_Kappa, jobs_list[c].head[0])
    q_Kappa_u=min(q_Kappa, jobs_list[c].tail[0])
    p_Kappa_u=p_Kappa+jobs_list[c].body[0]
    h_Kappa_u=r_Kappa_u+p_Kappa_u+q_Kappa_u
    
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
