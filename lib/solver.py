# -*- coding: utf-8 -*-
"""
Created in Mai 2024

@author: mertens, lucas
@email: lucas.mertens@fu-berlin.de
"""

import gurobipy as gp
from gurobipy import GRB
from lib.arc import Arc
from lib.node import Node

def solve_min_cost_flow(network):
  model = gp.Model("MCF")
  nodes = network.get_nodes()
  arcs = network.get_arcs()
  sink_node = Node(nodes[0].get_containing_persons(), False)
  circulation_flow_arc = Arc(sink_node, nodes[0],0)
  arcs.append(circulation_flow_arc)
  arcs_as_tuples = gp.tuplelist([arc.nodes_to_tuple() for arc in network.get_arcs()])
  
  x_arcs = model.addVars(arcs_as_tuples, name="x", vtype=GRB.BINARY)
  
  model.setObjective(sum(x_arcs[(arc.get_from_node(), arc.get_to_node())] * arc.get_travel_time() for arc in arcs), GRB.MINIMIZE)
  
  for node in nodes:
    model.addConstr(
      gp.quicksum(x_arcs[from_node, node] for from_node, to_node in arcs_as_tuples.select('*', node))
      ==
      gp.quicksum(x_arcs[node, to_node] for from_node, to_node in arcs_as_tuples.select(node, '*'))) 
    
  model.addConstr(x_arcs[circulation_flow_arc.nodes_to_tuple()] == 1)
  model.optimize()
  

  # There is probably a nicer way to sort the arcs
  origin_arcs = [arc for arc in arcs if arc.get_from_node().get_is_origin()]
  origin_arcs = sorted(origin_arcs, key=lambda x: len(x.get_from_node().get_containing_persons()), reverse=True)
  traveled_arcs_source = []
  for arc in origin_arcs:
    if x_arcs[(arc.get_from_node(),arc.get_to_node())].x < 0.1:
      continue
    traveled_arcs_source.append(arc)
    
  traveled_sink_arcs = []
  sink_arcs = [arc for arc in arcs if not arc.get_from_node().get_is_origin()]
  sink_arcs = sorted(sink_arcs, key=lambda x: len(x.get_from_node().get_containing_persons()))
  for arc in sink_arcs:
    if x_arcs[(arc.get_from_node(),arc.get_to_node())].x < 0.1:
      continue
    traveled_sink_arcs.append(arc)  
    
  traveled_arcs = []
  for i in range(len(traveled_arcs_source)):
    traveled_arcs.append(traveled_arcs_source[i])
    traveled_arcs.append(traveled_sink_arcs[i])
    
  
  print("Optimal solution")
  print("*******************")
  print("ROUTE:")
  print("*******************")
  total_travel_time = 0
  for arc in traveled_arcs:
    #Important, do not use == 0 or == 1 with Gurobi; for == 0 use .x < 0.1
    if x_arcs[(arc.get_from_node(),arc.get_to_node())].x < 0.1:
      continue
    if arc.get_travel_time() == 0:
      continue
    print("Total traveled time so far: " + str(total_travel_time))
    total_travel_time += arc.get_travel_time()
    if arc.get_from_node().get_is_origin():
      print("Currently not crossed the bridge: " + str(arc.get_from_node().get_containing_persons()))
      print("Sending: " + str(arc.get_persons_traveled_arc()) + " across the bridge")
    else:
      print("Currently crossed the bridge: " + str(arc.get_from_node().get_containing_persons()))
      print("Sending: " + str(arc.get_persons_traveled_arc())+ " back to get the others")
    print("This will take: " + str(arc.get_travel_time()) + " minutes")
    print("#####################")   
  
  print("Total traveled time: " + str(total_travel_time))
  print("#####################")   