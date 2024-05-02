# -*- coding: utf-8 -*-
"""
Created in Mai 2024

@author: mertens, lucas
@email: lucas.mertens@fu-berlin.de
"""

from lib.node import Node
from lib.arc import Arc
from lib.network import Network

#TODO: clean up redundant code and increase readability with methods
def add_arcs_and_nodes(from_node, network,number_of_people_to_cross_bridge):
  for person_index in from_node.get_containing_persons():
    if not from_node.get_is_origin():
      if len(from_node.get_containing_persons()) == number_of_people_to_cross_bridge:
        return
      persons_in_to_node = [i for i in range(1, number_of_people_to_cross_bridge+1) 
                            if i == person_index 
                            or i not in from_node.get_containing_persons()]
      to_node = Node(persons_in_to_node, not from_node.get_is_origin())
      arc = Arc(from_node, to_node, person_index)
      network.add_arc(arc)
      if to_node in network.get_nodes():
        continue
      network.add_node(to_node)
      add_arcs_and_nodes(to_node, network,number_of_people_to_cross_bridge)
      continue
    if len(from_node.get_containing_persons()) == 1:
      persons_in_to_node = [i for i in range(1, number_of_people_to_cross_bridge+1) ]
      to_node = Node(persons_in_to_node, not from_node.get_is_origin())
      arc = Arc(from_node, to_node, person_index)
      network.add_arc(arc)
      if to_node in network.get_nodes():
        continue
      network.add_node(to_node)
      continue
    for person_index2 in from_node.get_containing_persons():
      if person_index2 <= person_index:
        continue
      persons_in_to_node = [i for i in range(1, number_of_people_to_cross_bridge+1) 
                            if i == person_index 
                            or i == person_index2 
                            or i not in from_node.get_containing_persons()]

      to_node = Node(persons_in_to_node, not from_node.get_is_origin())
      arc = Arc(from_node, to_node, max(person_index, person_index2))
      network.add_arc(arc)
      if to_node in network.get_nodes():
        continue
      network.add_node(to_node)
      add_arcs_and_nodes(to_node, network, number_of_people_to_cross_bridge)


def create_network(number_of_people_to_cross_bridge):
  initial_node = Node([i for i in range(1,number_of_people_to_cross_bridge+1)])
  network = Network()
  network.add_node(initial_node)
  add_arcs_and_nodes(initial_node, network,number_of_people_to_cross_bridge)
  return network