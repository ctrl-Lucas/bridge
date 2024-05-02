import time
from lib import networkCreation
from lib import solver

if __name__ == "__main__":
    time_start = time.time()
    print('Start solving bridge problem...')
    print('Creating Nodes and Arcs first...')
    number_of_people_to_cross_bridge = 5
    network = networkCreation.create_network(number_of_people_to_cross_bridge)
    print('Network successfully created.')
    print('Number of nodes in the network: ', len(network.get_nodes()))
    print('Number of arcs in the network: ', len(network.get_arcs()))
    solver.solve_min_cost_flow(network)
    print('Successfully solved bridge problem.')
    print('Total execution time: ', time.time() - time_start, 'seconds.')
    
    # Now we get knowledge about the optimal solution, a simple heuristic
    # can surely skip the creation of arcs and nodes and directly solve the problem.
    # This would reduce computational time for large number of people to cross the bridge significantly