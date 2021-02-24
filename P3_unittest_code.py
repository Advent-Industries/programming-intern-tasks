from P3_input import Quadratic
import unittest

# How to call the quadratic function from the other file
# Use this information to create unit tests for the unit test software problem\
# you should create a class object and call this function within each of the test case
functionInstanceObject = Quadratic(1, 5, 6)
functionMethod = functionInstanceObject.calculateQuadratic()
# Changing something
'''
Three UNIT TEST CASES TO TESTT!!!
Test One: Test if 'a' value is equal to 

Test Two: 

Test Three: 

'''
class TestStringMethods(unittest.TestCase):
  def test_case_one(self):
    functionInstanceObjectOne = Quadratic(1, 5, 6)
    functionMethod = functionInstanceObjectOne.calculateQuadratic()
    # include code here to test whether the function output
    # use assert statements

  def test_case_two(self):
    functionInstanceObjectTwo = Quadratic(4, 2, 8)
    functionMethod = functionInstanceObjectTwo.calculateQuadratic()

  def test_case_three(self):
    functionInstanceObjectThree = Quadratic(24, 5, 9)
    functionMethod = functionInstanceObjectThree.calculateQuadratic()


