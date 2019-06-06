from ortools.linear_solver import pywraplp
from pathlib import Path
from ortools.sat.python import cp_model

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

    solver.SetTimeLimit(12000)
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
    print("MILP: ",instanceName,"Cmax:",solver.Objective().Value())
    pi=[]
    for i in range(len(starts)):
        pi.append((i,starts[i].solution_value()))
    pi.sort(key=lambda x: x[1])
    #print(pi)

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

def CP(jobs, instanceName):

    model_cp=cp_model.CpModel()

    variablesMaxValue=0
    for a in range(len(jobs)):
        variablesMaxValue += jobs[a].R + jobs[a].P + jobs[a].Q

    #variables:
    alfasMatrix={}#attention!dictionary−notlist!
    for i in range(len(jobs)):
        for j in range(len(jobs)):
            alfasMatrix[i,j]=model_cp.NewIntVar(0,1,"alfa"+str(i)+"_"+str(j)) #IntVar -> NewIntVar
    starts=[]
    for i in range(len(jobs)):
        starts.append(model_cp.NewIntVar(0,variablesMaxValue,"starts"+str(i)))
    cmax=model_cp.NewIntVar(0, variablesMaxValue, "cmax")


    #constraints:
    for i in range(len(jobs)):
        model_cp.Add(starts[i]>=jobs[i].R)
        model_cp.Add(cmax>=starts[i]+jobs[i].P+jobs[i].Q)
    for i in range(len(jobs)):
        for j in range(i+1,len(jobs)):
            model_cp.Add(starts[i]+jobs[i].P<=starts[j]
                +alfasMatrix[i,j]*variablesMaxValue)
            model_cp.Add(starts[j]+jobs[j].P<=starts[i]
                +alfasMatrix[j,i]*variablesMaxValue)
            model_cp.Add(alfasMatrix[i,j]+alfasMatrix[j,i]==1)

    # solver:
    model_cp.Minimize(cmax)
    solver = cp_model.CpSolver() #Solve() -> CpSolver()
    status = solver.Solve(model_cp)
    if (status is not cp_model.OPTIMAL):
        print("Notoptimal!")
    print("CP: ",instanceName, "Cmax:", solver.ObjectiveValue())
    pi = []
    for i in range(len(starts)):
        pi.append((i, solver.Value(starts[i]))) # 
    pi.sort(key=lambda x: x[1])
    #print(pi)
    
def main():
    file_paths = ['data000.txt', 'data001.txt','data002.txt', 'data003.txt','data004.txt', 'data005.txt','data006.txt', 'data007.txt','data008.txt',]
    for i in range(len (file_paths)):
        jobs = GetRPQsFromFile (file_paths[i])
        Milp(jobs, file_paths[i])
        CP(jobs, file_paths[i])

main()
