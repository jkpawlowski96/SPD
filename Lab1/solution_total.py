from job import Job
perm=[0,1,2]
j=[]

j.append(Job([2,3]))
j.append(Job([1,2]))
j.append(Job([3,1]))
j.append(Job([1,1]))
j.append(Job([2,1]))
#jakis przyklad

j[0].cmax(perm,j)


