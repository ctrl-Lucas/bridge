# -*- coding: utf-8 -*-
"""
Created in Mai 2024

@author: mertens, lucas
@email: lucas.mertens@fu-berlin.de
"""

class Node:
  def __init__(self, containing_persons =[], is_origin = True):
    self.__containing_persons = containing_persons
    self.__is_origin = is_origin

  def get_id(self):
    return self.__id
  
  def get_containing_persons(self):
    return self.__containing_persons
  
  def get_is_origin(self):
    return self.__is_origin
  
  def remove_person(self, person):
    if person not in self.__containing_persons:
      raise ValueError("Person not in node")
    self.__containing_persons.remove(person)
    
  def add_person(self, person):
    if person in self.__containing_persons:
      raise ValueError("Person already in node")
    self.__containing_persons.append(person)
    self.__containing_persons.sort()
    
  # Adding an ID to each Node Object would make the comparison easier and faster
  def __eq__(self, other):
    if not isinstance(other, Node):
      return False
    if self.__is_origin != other.get_is_origin():
      return False
    return self.__containing_persons == other.get_containing_persons() 
  
  def __hash__(self):
    return hash(str(self.__containing_persons) + str(self.__is_origin))     