# -*- coding: utf-8 -*-
"""
Created in Mai 2024

@author: mertens, lucas
@email: lucas.mertens@fu-berlin.de
"""

class Arc:
  def __init__(self, from_node, to_node, travel_time):
    self.__from_node = from_node
    self.__to_node = to_node
    self.__travel_time = travel_time
    
  def get_from_node(self):
    return self.__from_node
  
  def get_to_node(self):
    return self.__to_node
  
  def get_travel_time(self):
    return self.__travel_time
  
  def nodes_to_tuple(self):
    return (self.__from_node, self.__to_node)
    
  def get_persons_traveled_arc(self):
    return list(set(self.__from_node.get_containing_persons()).intersection(self.__to_node.get_containing_persons()))
  
  
    
    
  