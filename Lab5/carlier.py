from job import *
from schrage import schrange, schargepmtn
from schrage import cmax
import copy


def carlier_algorithm(jobs_list, UB, LB):
    global pi_prim

    if(UB!=LB):
        pi, U = schrange(copy.deepcopy(jobs_list))
        LB_prim=schargepmtn(jobs_list)
        if U < UB:
            UB = U
            pi_prim = copy.deepcopy(pi)
        

        #print(LB_prim, UB)
        ind_c=-1
        tab=cmax_tab(jobs_list, pi) #tablica zakonczenia wykonywania (p) kolejnych zadan
        tab_end=[]
        for j in range(len(tab)):
            tab_end.append(tab[j]+jobs_list[pi[j]].tail[0])
        Cmax_val=max(tab_end)
        #wyznaczenie b
        for i in range(len(pi)):
            if Cmax_val==tab[i]+jobs_list[pi[i]].tail[0]:
                b=pi[i]
                ind_b=i

        #wyznaczenie a
        ind_a=-1
        for i in range(len(pi)):
            suma=0
            for s in range(i, ind_b+1):
                suma=suma+jobs_list[pi[s]].body[0]
            if Cmax_val==jobs_list[pi[i]].head[0]+suma+jobs_list[b].tail[0]:
                if ind_a==-1:
                    a=pi[i]
                    ind_a=i

        #wyznaczenie c
        for i in range(ind_a, ind_b+1):
            if jobs_list[pi[i]].tail[0]<jobs_list[b].tail[0]:
                c=pi[i]
                ind_c=i

        
        #jesli nie znaleziono c
        if ind_c == -1:
            return pi_prim, UB, LB
        
        #wyznaczenie bloku
        Kappa=[]
        for i in range(ind_c+1, ind_b+1):
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

        '''
        L=[]
        for i in range(ind_c+1):
            if jobs_list[pi[i]].body[0]>UB-h_Kappa:
                L.append(i)
        for i in range(ind_b+1, len(pi)):
            if jobs_list[pi[i]].body[0]>UB-h_Kappa:
                L.append(i)

        for i in L:
            jobs_list[pi[i]].head[0]=max(jobs_list[pi[i]].head[0], r_Kappa+p_Kappa)
        for i in L:
            if r_Kappa+jobs_list[pi[i]].body[0]+p_Kappa>=UB:
                jobs_list[pi[i]].tail[0]=max(jobs_list[pi[i]].tail[0],q_Kappa+p_Kappa)
        '''
        #lewy potomek - zmiana wartosci r zadania krytycznego 
        old_rc=jobs_list[c].head[0]  
        jobs_list[c].head[0]=max(jobs_list[c].head[0], r_Kappa+p_Kappa)
        Upmtn= schargepmtn(copy.deepcopy(jobs_list))
        #Kappa u {c}
        r_Kappa_u=min(r_Kappa, jobs_list[c].head[0])
        q_Kappa_u=min(q_Kappa, jobs_list[c].tail[0])
        p_Kappa_u=p_Kappa+jobs_list[c].body[0]
                
        h_Kappa_u=r_Kappa_u+p_Kappa_u+q_Kappa_u
                
        LB=max(h_Kappa, h_Kappa_u, LB)
        if LB<UB: #jesli jest sens...
            pi, UB, LB = carlier_algorithm(jobs_list, UB, LB)
        #powrot z wartoscia r
        jobs_list[c].head[0]=old_rc


        #prawy potomek - zmiana wartosci q zadania krytycznego
        
        old_qc=jobs_list[c].tail[0]
        jobs_list[c].tail[0]=max(jobs_list[c].tail[0], q_Kappa+p_Kappa)
        Upmtn= schargepmtn(copy.deepcopy(jobs_list))
        #Kappa u {c}
        r_Kappa_u=min(r_Kappa, jobs_list[c].head[0])
        q_Kappa_u=min(q_Kappa, jobs_list[c].tail[0])
        p_Kappa_u=p_Kappa+jobs_list[c].body[0]
                
        h_Kappa_u=r_Kappa_u+p_Kappa_u+q_Kappa_u
             
        LB=max(h_Kappa, h_Kappa_u, LB)
        if LB<UB: #jesli jest sens...
            pi, UB, LB = carlier_algorithm(jobs_list, UB, LB)

        #powrot z wartoscia q
        jobs_list[c].tail[0]=old_qc
    return pi, UB, LB

    
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
