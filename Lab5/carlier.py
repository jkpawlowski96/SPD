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

    Rpi = [R[i] for i in pi]
    Ppi = [P[i] for i in pi]
    Qpi = [Q[i] for i in pi]
    Cpi = [C[i] for i in pi]


    #wyznaczenie b
    b=[]
    J = list(range(1, len(pi)))
    for j in J:
        if cmax_pi == (Cpi[j] + Qpi[j]):
            b.append(j)
    b = max(b)

    #wyznaczenie a
    a =[]
    for j in J:
        sum_jb = sum([Ppi[s] for s in range(j, b+1)])
        if cmax_pi == (Rpi[j] + sum_jb + Qpi[b]):
            a.append(j)
    a = min(a)

    #wyznaczenie c
    c = []
    J = list(range(a, b+1))
    for j in J:
        if Qpi[j] < Qpi[b]:
            c.append(j)

    # jesli nie znaleziono c
    if len(c)==0:
        return pi_prim

    c = max(c)

    K = list(range(c+1, b+1))

    old = jobs_list[pi[c]].head[0]
    rk=min([Rpi[i] for i in K])
    qk=min([Qpi[i] for i in K])
    pk=sum([Ppi[i] for i in K])

    jobs_list[pi[c]].head[0] = max(Rpi[c], rk + pk)
    LB = schargepmtn(jobs_list)
    #hK = [R[i]+P[i]+Q[i] for i in K]
    #hKc = hK.append(R[c]+P[c]+Q[c])

    #LB = max(hK, hKc, LB)

    if LB < UB:
        carlier_algorithm(jobs_list.copy(), UB.copy())
    jobs_list[pi[c]].head[0] = old

    ########
    old = jobs_list[pi[c]].tail[0]
    jobs_list[pi[c]].tail[0] = max(Qpi[c], qk + pk)

    LB = schargepmtn(jobs_list)
    #hK = [R[i] + P[i] + Q[i] for i in K]
    #hKc = hK.append(R[c] + P[c] + Q[c])

    #LB = max(hK, hKc, LB)

    if LB < UB:
        carlier_algorithm(jobs_list.copy(), UB.copy())
    jobs_list[pi[c]].tail[0] = old

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





