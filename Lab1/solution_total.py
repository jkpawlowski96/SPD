from job import Job
def swap(a,b):
    return b, a

def perm(k,P): #k jest potrzebne do rekurencji, bo permutacje chyba najlatwiej przez rekurencje wyznaczyc
    #moze jest jakas gotowa biblioteka? Nie chcialo mi sie szukac, ogolnie odpal to sobie, odkomentowujac
    #kolejny przyklad (linie 21-25) i zobacz jak to wyglada, gdyby udalo sie wrzucic to do p, przeglad zupelny bylby ok
    if k==1:
        print(P) #umiesz jakos to wrzucic do p? :(

    else: #jesli zostalo wiecej niz 1 element do pozamieniania
        for i in range(0,k):
            P[i],P[k-1]=swap(P[i],P[k-1]) #zamiana pierwszego z ostatnim
            perm(k-1,P) #permutacja k-1 elementow (k-ty jest juz dobrze ustawiony)
            P[i],P[k-1]=swap(P[i],P[k-1]) # i powrot do pierwotnego polozenia

pr=[0,1,2] #przykladowa permutacja
j=[]

#jakis przyklad
j.append(Job([2,3]))
j.append(Job([1,2]))
j.append(Job([3,1]))
#j.append(Job([1,1]))
#j.append(Job([2,1]))

p=[]
P = [] #permutacja potrzebna do perm
for i in range(0, len(j)): #powinna byc wypelniona liczbami, ktore chcemy pozamieniac, u nas indeksy zadan, czyli od 0 do ilosci zadan
    P.append(i)

perm(len(j),P) #i wywolanie

for i in range(len(p)): #a tutaj, gdyby permutacje byly zapisane w p, to wyswietla czasy zakoczenia dla konkretnej kolejnosci zadan
    print("%s ---> %d"%(str(p[i]),j[0].cmax(p[i],j)))