from __future__ import print_function
from ortools.linear_solver import pywraplp

# Create the mip solver with the CBC backend.
solver = pywraplp.Solver('simple_mip_program',
                         pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

infinity = solver.infinity()
# x and y are integer non-negative variables.
x = solver.IntVar(0.0, infinity, 'x')
y = solver.IntVar(0.0, infinity, 'y')

print('Number of variables = ', solver.NumVariables())

# x + 7 * y <= 17.5.
solver.Add(x + 7 * y <= 17.5)

# x <= 3.5.
solver.Add(x <= 3.5)

print('Number of constraints = ', solver.NumConstraints())

# Maximize x + 10 * y.
solver.Maximize(x + 10 * y)

result_status = solver.Solve()
# The problem has an optimal solution.
assert result_status == pywraplp.Solver.OPTIMAL

# The solution looks legit (when using solvers others than
# GLOP_LINEAR_PROGRAMMING, verifying the solution is highly recommended!).
assert solver.VerifySolution(1e-7, True)

print('Solution:')
print('Objective value = ', solver.Objective().Value())
print('x = ', x.solution_value())
print('y = ', y.solution_value())
