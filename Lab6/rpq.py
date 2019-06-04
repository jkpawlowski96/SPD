from ortools.linear_solver import pywraplp
from pathlib import Path


class RPQ():
    def __init__(self,r,p,q):
        self.R=r
        self.P=p
        self.Q=q


def Milp(jobs,instanceName):
    variablesMaxValue=0
    for i in range(len(jobs)):
        variablesMaxValue+=(jobs[i].R+jobs[i].P+jobs[i].Q)
    solver=pywraplp.Solver('simple_mip_program',
    pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    #variables:
    alfasMatrix={}#attention!dictionary−notlist!
    for i in range(len(jobs)):
        for j in range(len(jobs)):
            alfasMatrix[i,j]=solver.IntVar(0,1,"alfa"+str(i)+"_"+str(j))
    starts=[]
    for i in range(len(jobs)):
        starts.append(solver.IntVar(0,variablesMaxValue,"starts"+str(i)))
    cmax=solver.IntVar(0,variablesMaxValue,"cmax")
    
    #constraints:
    for i in range(len(jobs)):
        solver.Add(starts[i]>=jobs[i].R)
        solver.Add(cmax>=starts[i]+jobs[i].P+jobs[i].Q)
    for i in range(len(jobs)):
        for j in range(i+1,len(jobs)):
            solver.Add(starts[i]+jobs[i].P<=starts[j]
                +alfasMatrix[i,j]*variablesMaxValue)
            solver.Add(starts[j]+jobs[j].P<=starts[i]
                +alfasMatrix[j,i]*variablesMaxValue)
            solver.Add(alfasMatrix[i,j]+alfasMatrix[j,i]==1)

    #solver:
    solver.Minimize(cmax)
    status=solver.Solve()
    if(status is not pywraplp.Solver.OPTIMAL):
        print("Notoptimal!")
    print(instanceName,"Cmax:",solver.Objective().Value())
    pi=[]
    for i in range(len(starts)):
        pi.append((i,starts[i].solution_value()))
    pi.sort(key=lambda x: x[1])
    print(pi)

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
            jobs_list.append(RPQ(values[0], values[1], values[2]))
        return jobs_list


def main():
    file_paths = [ 'in000.txt','in50.txt','in100.txt']
    for i in range(len (file_paths)):
        jobs = GetRPQsFromFile (file_paths[i])
        Milp(jobs, file_paths[i])

main()