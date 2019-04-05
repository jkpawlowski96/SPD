"""
SA algorithm
"""
global k=0
global k_max=10
global mi=0.95

def sa(perm0, T0):
    global k=0
    # Step 1 Initialization by parameters
    perm = perm0
    T = T0
    # Step 2 Generate move
    while True:
        perm1 = swap(perm)
        # Step 3 Apply or not apply move
        proba = move_proba(cmax(perm), cmax(perm1), T)
        if proba >= randint(0,1)
            perm = perm1
        # Step 4 cool down    
        T = cool1(T)  
        # Step 5 Stop criterion
        if k == k_max:
            break
        else:
            k = k + 1
            continue 


def move_proba(c, c1, T):
    if c1 >= c:
        return exp((c-c1)/T)
    else:
        return 1


def swap(perm)
    x = rand(len(perm))
    y = rand(len(perm))
    tmp=perm[x]
    perm[x]=perm[y]
    perm[y]=tmp
    return perm


def cool1(T):
    global mi
    return mi*T

def cool2(T):
    global k, k_max
    return T*(k/k_max)    