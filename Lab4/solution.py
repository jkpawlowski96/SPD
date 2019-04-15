from job import *

jobs_list=test_jobs(3,2)

for i in range (len(jobs_list)):
    for j in range (jobs_list[0].size):
        print('job: ',i,' machine: ',j)
        print('        times -> ', jobs_list[i].time(j))
print(num_of_machines(jobs_list))

del(jobs_list)
jobs_list=jobs_load('../dane_testowe_RPQ/in200.txt')
for i in range (len(jobs_list)):
    for j in range (jobs_list[0].size):
        print(jobs_list[i].time(j))
print(num_of_machines(jobs_list))
