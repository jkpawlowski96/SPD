"""
SA algorithm
"""
from algorithm_cmax import cmax
from random import randint
from math import exp

k = 0
k_max = 10
mi = 0.95


def sa(perm0, t0):
    """
    SA algorithm
    :param perm0:
    :param t0:
    :return:
    """

    global k
    # Step 1 Initialization by parameters
    perm = perm0
    t = t0
    # Step 2 Generate move
    while True:
        perm1 = swap(perm)
        # Step 3 Apply or not apply move
        proba = move_proba(cmax(perm), cmax(perm1), t)
        if proba >= randint(0,1):
            perm = perm1
        # Step 4 cool down    
        t = cool1(t)
        # Step 5 Stop criterion
        if k == k_max:
            break
        else:
            k = k + 1
            continue 


def move_proba(c, c1, t):
    """
    Chance 0 to 1 of move perm <- perm'
    :param c: cmax(pi)
    :param c1: cmax(pi')
    :param t: time T
    :return:
    """
    if c1 >= c:
        return exp((c-c1)/t)
    else:
        return 1


def swap(perm):
    """
    Change positions of 2 random elements
    :param perm: permutation (pi)
    :return:
    """
    x = randint(0, len(perm)-1)
    y = randint(0, len(perm)-1)
    tmp = perm[x]
    perm[x] = perm[y]
    perm[y] = tmp
    return perm


def cool1(t):
    """
    Cool down by mi*T
    :param t: time T
    :return:
    """
    global mi
    return mi*t


def cool2(t):
    """
    Cool down by iterable
    :param t: time T
    :return:
    """
    global k, k_max
    return t*(k/k_max)
