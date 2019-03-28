from itertools import *
from algorithms import *
import time as t

clock=0#clock

def mtime(opt='start'):
    global clock

    if opt == 'start':
        clock =t.time()

    if opt =='stop':
        clock = t.time()-clock
        #print('Measured time:',clock,'s')
        return clock
    
#Load jobs from file
jobs_list=jobs_load('./ta/ta001.txt')

#print('NEH: ',NEH(jobs_list))
#print('QNEH: ',QNEH(jobs_list))

latex=open("latex2.txt", "w")
plik=[]
for i in range(121):
    if i<10:
        nazwa='./ta/ta00'+str(i)+'.txt'
    elif i<100:
        nazwa='./ta/ta0'+str(i)+'.txt'
    else:
        nazwa='./ta/ta'+str(i)+'.txt'
    plik.append(nazwa)

for i in range(len(plik)):
    print(plik[i])
    #Load jobs from file
    jobs_list=jobs_load(plik[i])
    '''
    mtime('start')
    orderjohn=AlgJohn(jobs_list)
    time_algjohn=mtime('stop')
    mtime('start')
    orderneh=NEH(jobs_list)
    time_neh=mtime('stop')
    '''

    mtime('start')
    orderqneh=QNEH(jobs_list)
    time_qneh=mtime('stop')
    if i<10:
        nazwa='ta00'+str(i)+'.txt'
    elif i<100:
        nazwa='ta0'+str(i)+'.txt'
    else:
        nazwa='ta'+str(i)+'.txt'

    #cmaxj=c_max(orderjohn, jobs_list)
    #cmaxn=c_max(orderneh, jobs_list)
    #latex.write("%s ,&, %.3f ,&,%d,&, %.3f ,&,%d \n" %(nazwa, time_algjohn*1000, cmaxj, time_neh*1000, cmaxn))
    latex.write("%.3f,&,%.3f \n" %(time_qneh, c_max(orderqneh,jobs_list)))
latex.close()

