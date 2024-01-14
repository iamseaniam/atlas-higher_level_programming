#!/usr/bin/python3
"""
This is a module for demonstrating classes in Python.
"""


class Square:
  """
  This class represents a square. It has a private attribute '__size' which represents the size of the square.
  The size of the square is set during instantiation and cannot be changed afterwards.
  """
  def __init__(self, size):
      self.__size = size
      