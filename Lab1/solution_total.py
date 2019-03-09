from job import Job
def swap(a,b):
    return b, a

def perm(k,P):
    if k==1:
        print(P) #umiesz jakos to wrzucic do p? :(

    else:
        for i in range(0,k):
            P[i],P[k-1]=swap(P[i],P[k-1])
            perm(k-1,P)
            P[i],P[k-1]=swap(P[i],P[k-1])

pr=[0,1,2]
j=[]

#jakis przyklad
j.append(Job([2,3]))
j.append(Job([1,2]))
#j.append(Job([3,1]))
#j.append(Job([1,1]))
#j.append(Job([2,1]))

p=[]
P = []
akt=[]
for i in range(0, len(j)):
    P.append(i)
perm(len(j),P)

for i in range(len(p)):
    print("%s ---> %d"%(str(p[i]),j[0].cmax(p[i],j)))