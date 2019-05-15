from job import *
from schrage import schargepmtn, schrange
from schrage import cmax as max_c

def carlier_algorithm(tasks, UB):
    tasks = tasks.copy()
    pi = schrange(tasks)
    pi_prim = []
    U = max_c(tasks, pi)
    if U < UB:
        UB = U
        pi_star = pi
    b = -1
    a = -1
    c = -1
    for i in range(len(pi)):
        if (c_(tasks, pi[:(i+1)]) + tasks[pi[i][0]][2]) == U:
            b = i
    for i in range(len(pi)):
        p_list = [tasks[pi[j][0]][1] for j in range(i, b+1)]
        if tasks[pi[i][0]][0] + sum(p_list) + tasks[pi[b][0]][2] == U:
            a = i
            break
    for i in range(a, b+1):
        if tasks[pi[i][0]][2] < tasks[pi[b][0]][2]:
            c = i
    if c == -1:
        return pi_star
    r_prim = tasks[min(pi[c+1:b+1], key=lambda x: tasks[x[0]][0])[0]][0]
    q_prim = tasks[min(pi[c+1:b+1], key=lambda x: tasks[x[0]][2])[0]][2]
    p_list = [tasks[pi[j][0]][1] for j in range(b, c+2)]
    p_prim = sum(p_list)
    old_c = tasks[pi[c][0]]
    tasks[pi[c][0]] = (max(tasks[pi[c][0]][0], r_prim + p_prim), tasks[pi[c][0]][1], tasks[pi[c][0]][2])
    LB = max_c(tasks, schargepmtn(tasks))
    if LB < UB:
        pi_prim = carlier_algorithm(tasks, UB)
    tasks[pi[c][0]] = old_c
    old_c = tasks[pi[c][0]][2]
    tasks[pi[c][0]] = (tasks[pi[c][0]][0], tasks[pi[c][0]][1], max(tasks[pi[c][0]][2], q_prim + p_prim))
    LB = max_c(tasks, schargepmtn(tasks))
    if LB < UB:
        pi_prim = carlier_algorithm(tasks, UB)
    tasks[pi[c][0]] = old_c
    return pi_prim


def c_(tasks, order):
    actual_time = 0
    min_time = 0
    for task in order:
        actual_time += task[1]
    return actual_time