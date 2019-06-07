from __future__ import print_function
import collections
from ortools.sat.python import cp_model


def Cp(jobs, instanceName):
    model_cp = cp_model.CpModel()
    nom = 1 + max(task[0] for job in jobs for task in job)
    machines = range(nom)

    variablesMaxValue = sum(task[1] for job in jobs for task in job)

    #krotka do przechowywanie info o stworzonych zmienych, start, end, interval
    task_type = collections.namedtuple('task_type', 's e i')
    
    tasks = {}
    machine_to_intervals = collections.defaultdict(list)
    cmax = model_cp.NewIntVar(0, variablesMaxValue, 'cmax')
    
    for job_id, job in enumerate(jobs):
        for task_id, task in enumerate(job):
            
            starts = model_cp.NewIntVar(0, variablesMaxValue, 'start' + '_'+str(job_id)+'_'+str(task_id))
            ends = model_cp.NewIntVar(0, variablesMaxValue, 'end' + '_'+str(job_id)+'_'+str(task_id))
            intervals = model_cp.NewIntervalVar(starts, task[1], ends,
                                                'interval' + '_'+str(job_id)+'_'+str(task_id))
            tasks[job_id, task_id] = task_type(s=starts, e=ends, i=intervals)
            machine_to_intervals[task[0]].append(intervals)

    #constrains
    
    for machine in machines: #jedno zadanie na jednej maszynie w danym momencie
        model_cp.AddNoOverlap(machine_to_intervals[machine])


    # S_{i+1,j}>=C_{i,j} oraz cmax>=C_{i,j}
    for job_id, job in enumerate(jobs):
        for task_id in range(len(job) - 1):
            model_cp.Add(tasks[job_id, task_id + 1].s >= tasks[job_id, task_id].e)
            model_cp.Add(cmax>=tasks[job_id, task_id+1].e)
    
    #solver
    model_cp.Minimize(cmax)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 5*60.0
    status = solver.Solve(model_cp)

    if(status is not cp_model.OPTIMAL):
        print("Notoptimal!")
    print("  CP: ",instanceName,"Cmax:",solver.ObjectiveValue())
    
def GetINSAdataFromFile(filePath):
    filePath = './dane_testowe_Jobshop/' + filePath
    plik = open(filePath)
    zawartosc = plik.read()
    dane = list(map(int, zawartosc.split()))  # zmiana string na int
    liczbaZadan = dane[0]
    liczbaMaszyn = dane[1]
    liczbaOperacji = dane[2]
    #print(liczbaZadan, liczbaMaszyn)
    dane.pop(0)
    dane.pop(0)
    dane.pop(0)
    job = []
    jobs = []
    for i in range(liczbaZadan):
        liczbaOperacjiZadania = dane[0]
        dane.pop(0)
        for j in range(liczbaOperacjiZadania):
            job.append([dane[0]-1, dane[1]])
            dane.pop(0)
            dane.pop(0)
        jobs.append(0)
        jobs[i] = job[:]
        for k in range(len(job)):
            job.pop()

    return jobs


if __name__ == '__main__':
    file_paths = ["data000.txt","data001.txt","data002.txt","data003.txt","data004.txt","data005.txt","data006.txt","data007.txt","data008.txt","data009.txt","data010.txt","data011.txt","data012.txt"]
    #file_paths=["jobshop.txt"]
    for i in range(len(file_paths)):
        jobs = GetINSAdataFromFile(file_paths[i])
        Cp(jobs, file_paths[i])
