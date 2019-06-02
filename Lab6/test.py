# [START program]
from __future__ import print_function
# [START import]
from ortools.linear_solver import pywraplp

# [END import]


def IntegerProgrammingExample():
    """Integer programming sample."""
    # [START solver]
    # Create the mip solver with the CBC backend.
    solver = pywraplp.Solver('IntegerProgrammingExample',
                             pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    # [END solver]

    # [START variables]
    # x, y, and z are non-negative integer variables.
    x = solver.IntVar(0.0, solver.infinity(), 'x')
    y = solver.IntVar(0.0, solver.infinity(), 'y')
    z = solver.IntVar(0.0, solver.infinity(), 'z')
    # [END variables]

    # [START constraints]
    # 2*x + 7*y + 3*z <= 50
    constraint0 = solver.Constraint(-solver.infinity(), 50)
    constraint0.SetCoefficient(x, 2)
    constraint0.SetCoefficient(y, 7)
    constraint0.SetCoefficient(z, 3)

    # 3*x - 5*y + 7*z <= 45
    constraint1 = solver.Constraint(-solver.infinity(), 45)
    constraint1.SetCoefficient(x, 3)
    constraint1.SetCoefficient(y, -5)
    constraint1.SetCoefficient(z, 7)

    # 5*x + 2*y - 6*z <= 37
    constraint2 = solver.Constraint(-solver.infinity(), 37)
    constraint2.SetCoefficient(x, 5)
    constraint2.SetCoefficient(y, 2)
    constraint2.SetCoefficient(z, -6)
    # [END constraints]

    # [START objective]
    # Maximize 2*x + 2*y + 3*z
    objective = solver.Objective()
    objective.SetCoefficient(x, 2)
    objective.SetCoefficient(y, 2)
    objective.SetCoefficient(z, 3)
    objective.SetMaximization()
    # [END objective]

    # Solve the problem and print the solution.
    # [START print_solution]
    solver.Solve()
    # Print the objective value of the solution.
    print('Maximum objective function value = %d' % solver.Objective().Value())
    print()
    # Print the value of each variable in the solution.
    for variable in [x, y, z]:
        print('%s = %d' % (variable.name(), variable.solution_value()))
    # [END print_solution]


IntegerProgrammingExample()
# [END program]