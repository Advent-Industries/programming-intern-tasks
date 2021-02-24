from P3_input import Quadratic
from P3_unittest_code import TestStringMethods
import unittest

class Advent:
  def __init__(self):
    self.introductionMessage = "Hello Prospective Advent Industries Programming Interns! Attached in this same folder/directory are additional files that should help you with your programming tasks!"
  def softwareTaskOne(self):
    # view P1_input.txt 
    # view P1_output.txt
    pass
  def softwareTaskTwo(self):
    # Use Online Research!  
    # Modify Online solutions, openCV cannot be used in repl.it
    # Write a seperate python file to solve this problem
    pass
  def softwareTaskThree(self):
    unittest.main()
  def __str__(self):
    return self.introductionMessage
if __name__ == "__main__":
  instance = Advent()
  print(instance, "\n")

  # start editing code here 
  # Comment out the task you are not testing
  instance.softwareTaskOne()
  instance.softwareTaskThree()