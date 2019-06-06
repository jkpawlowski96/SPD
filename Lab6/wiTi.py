from ortools.linear_solver import pywraplp
from pathlib import Path
from ortools.sat.python import cp_model

class wiTi():
    def __init__(self,p,w,d):
        self.P=p
        self.W=w
        self.D=d

def GetRPQsFromFile(file_path):
    file_path = './dane_testowe_RPQ/' + file_path
    with open(file_path, 'r') as f:
        jobs_list = []
        lines = []
        # PARAMETERS
        for line in f:
            lines.append(line)

        # param=lines.pop(0).strip().split('   ')
        # jobs=int(param[0].strip())
        # cols=int(param[1].strip())
        # del param
        """Load times"""
        for line in lines:
            if 'str' in line:
                break
            line.rstrip().split('   ')
            line = line.split()
            if len(line)<3:
                continue
            values = [int(i) for i in line]
            jobs_list.append(wiTi(values[0], values[1], values[2]))
        return jobs_list
    

def Milp(jobs,instanceName):
    variablesMaxValue=0
    time=0
    for i in range(len(jobs)):
        time+=jobs[i].P
    for i in range(len(jobs)):
        if(time-jobs[i].D>0):
            variablesMaxValue+=(jobs[i].W*(time-jobs[i].D))
    solver=pywraplp.Solver('simple_mip_program',
    pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    solver.SetTimeLimit(12000)
    
    #variables:
    alfasMatrix={}#attention!dictionary−notlist!
    for i in range(len(jobs)):
        for j in range(len(jobs)):
            alfasMatrix[i,j]=solver.IntVar(0,1,"alfa"+str(i)+"_"+str(j))
    starts=[]
    ends=[]
    delays=[]
    for i in range(len(jobs)):
        starts.append(solver.IntVar(0,variablesMaxValue,"starts"+str(i)))
        ends.append(solver.IntVar(0,variablesMaxValue,"ends"+str(i)))
        delays.append(solver.IntVar(0,variablesMaxValue,"delays"+str(i)))
        
    wiTi=solver.IntVar(0,variablesMaxValue,"wiTi")
    
    #constraints:
    for i in range(len(jobs)):
        solver.Add(ends[i]>=starts[i]+jobs[i].P)
        solver.Add(delays[i]==jobs[i].W*(ends[i]-jobs[i].D))
        
    for i in range(len(jobs)):
        for j in range(i+1,len(jobs)):
            solver.Add(starts[i]+jobs[i].P<=starts[j]
                +alfasMatrix[i,j]*variablesMaxValue)
            solver.Add(starts[j]+jobs[j].P<=starts[i]
                +alfasMatrix[j,i]*variablesMaxValue)
            solver.Add(alfasMatrix[i,j]+alfasMatrix[j,i]==1)

    for i in range(len(delays)):
        wiTi+=delays[i]
    #solver:
    solver.Minimize(wiTi)
    status=solver.Solve()
    if(status is not pywraplp.Solver.OPTIMAL):
        print("Notoptimal!")
    print("MILP: ",instanceName,"Cmax:",solver.Objective().Value())
    pi=[]
    for i in range(len(starts)):
        pi.append((i,starts[i].solution_value()))
    pi.sort(key=lambda x: x[1])
    #print(pi)

def main():
    file_paths = ['witi1.txt','witi2.txt','witi3.txt','witi4.txt','witi5.txt','witi6.txt','witi7.txt','witi8.txt','witi9.txt','witi10.txt','witi11.txt',]
    for i in range(len (file_paths)):
        jobs = GetRPQsFromFile (file_paths[i])
        Milp(jobs, file_paths[i])

main()
