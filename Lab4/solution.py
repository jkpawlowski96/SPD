from job import *
from schrage import *

jobs_list = jobs_load('./dane_testowe_RPQ/in50.txt')
order0 = range(len(jobs_list))
order, cmax = schrange(jobs_list)
print('in50.txt',cmax)

jobs_list = jobs_load('./dane_testowe_RPQ/in100.txt')
order0 = range(len(jobs_list))
order, cmax = schrange(jobs_list)
print('in100.txt',cmax)

jobs_list = jobs_load('./dane_testowe_RPQ/in200.txt')
order0 = range(len(jobs_list))
order, cmax = schrange(jobs_list)
print('in200.txt',cmax)

jobs_list = jobs_load('./dane_testowe_RPQ/in50.txt')
order0 = range(len(jobs_list))
cmax = schargepmtn(jobs_list)
print('scharge pmtn in50.txt',cmax)

jobs_list = jobs_load('./dane_testowe_RPQ/in100.txt')
order0 = range(len(jobs_list))
cmax = schargepmtn(jobs_list)
print('scharge pmtn in100.txt',cmax)

jobs_list = jobs_load('./dane_testowe_RPQ/in200.txt')
order0 = range(len(jobs_list))
cmax = schargepmtn(jobs_list)
print('scharge pmtn in200.txt',cmax)


jobs_list = jobs_load('./dane_testowe_RPQ/in50.txt')
order0 = range(len(jobs_list))
order, cmax = schrange_nlogn(jobs_list)
print('in50.txt',cmax)

jobs_list = jobs_load('./dane_testowe_RPQ/in100.txt')
order0 = range(len(jobs_list))
order, cmax = schrange_nlogn(jobs_list)
print('in100.txt',cmax)

jobs_list = jobs_load('./dane_testowe_RPQ/in200.txt')
order0 = range(len(jobs_list))
order, cmax = schrange_nlogn(jobs_list)
print('in200.txt',cmax)

jobs_list = jobs_load('./dane_testowe_RPQ/in50.txt')
order0 = range(len(jobs_list))
cmax = schargepmtn_nlogn(jobs_list)
print('scharge pmtn in50.txt',cmax)

jobs_list = jobs_load('./dane_testowe_RPQ/in100.txt')
order0 = range(len(jobs_list))
cmax = schargepmtn_nlogn(jobs_list)
print('scharge pmtn in100.txt',cmax)

jobs_list = jobs_load('./dane_testowe_RPQ/in200.txt')
order0 = range(len(jobs_list))
cmax = schargepmtn_nlogn(jobs_list)
print('scharge pmtn in200.txt',cmax)