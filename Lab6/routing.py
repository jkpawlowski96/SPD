from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

# Distance callback
def create_distance_callback(dist_matrix):
  # Create a callback to calculate distances between cities.

  def distance_callback(from_node, to_node):
    return int(dist_matrix[from_node][to_node])

  return distance_callback

def main():
  # Cities
  city_names = ["Boston", "New York City", "Baltimore", "Pittsburg", "Syracuse"]

  # Distance matrix
  dist_matrix = [
      [0, 215, 402, 572, 311], #Boston
      [215, 0, 203, 371, 247], #New York City
      [402, 203, 0, 248, 332], #Baltimore
      [572, 371, 248, 0, 361], #Pittsburg
      [311, 247, 332, 361, 0]] #Syracuse

  tsp_size = len(city_names)
  num_routes = 1
  depot = 1

  # Create routing model
  if tsp_size > 0:
    routing = pywrapcp.RoutingModel(tsp_size, num_routes, depot)

    search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
    # Create the distance callback.
    dist_callback = create_distance_callback(dist_matrix)
    routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
    # Solve the problem.
    assignment = routing.SolveWithParameters(search_parameters)
    if assignment:
      # Solution distance.
      print ("Total distance: " + str(assignment.ObjectiveValue()) + " miles\n")
      # Display the solution.
      # Only one route here; otherwise iterate from 0 to routing.vehicles() - 1
      route_number = 0
      index = routing.Start(route_number) # Index of the variable for the starting node.
      route = ''
      while not routing.IsEnd(index):
        # Convert variable indices to node indices in the displayed route.
        route += str(city_names[routing.IndexToNode(index)]) + ' -> '
        index = assignment.Value(routing.NextVar(index))
      route += str(city_names[routing.IndexToNode(index)])
      print ("Route:\n\n" + route)
    else:
      print ('No solution found.')
  else:
    print ('Specify an instance greater than 0.')


main()
