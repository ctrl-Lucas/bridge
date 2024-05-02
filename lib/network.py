# -*- coding: utf-8 -*-
"""
Created in Mai 2024

@author: mertens, lucas
@email: lucas.mertens@fu-berlin.de
"""

class Network:
  def __init__(self):
    self.__nodes = []
    self.__arcs = []
    
  def add_node(self, node):
    self.__nodes.append(node)
    
  def add_arc(self, arc):
    self.__arcs.append(arc)
  
  def get_nodes(self):
    return self.__nodes
  
  def get_arcs(self):
    return self.__arcs
  
    
  