from P3_input import Quadratic
import unittest

# How to call the quadratic function from the other file
# Use this information to create unit tests for the unit test software problem\
# you should create a class object and call this function within each of the test case

# # # # # # 
# functionInstanceObject = Quadratic(1, 5, 6)
# output = functionInstanceObject.calculateQuadratic()
# # # # # # 

'''
THREE UNIT TEST CASES TO TESTT!!! (the first is done for you as an example)
You should modify the code inside the funcitons for unit_testing. Once you complete the unittests, determine if there are any problems/errors with the calculateQuadratic() method and fix them. If you manage to fix all errors and create all unit tests, there is another hidden error within the calculateQuadratic() program. Fixing this error demonstrates an advanced understanding of python programming! 

Test One: Test if 'solutions' option is equal to the string 'The solutions are (-3+0j) and (-2+0j)' using self.assertEqual

Test Two: Test if 'd' is equal to the actual discriminant using using self.assertEqual for a variety of test cases as specified in the function

Test Three: Test if 'a' option is of integer type using self.assertTrue and type(int) for various test cases as specified in the function

Test Four: Test anything you want (using an assert statement) to make sure that there are no errors in the quadratic solver program.
'''

class TestStringMethods(unittest.TestCase):
  def test_case_one(self):
    print("\n\n****Testing final solution output...****")
    print("****Choose Option 5 for this test****\n")

    '''
    Original Code (below)
      functionInstanceObjectOne = Quadratic(1, 5, 6)
      output = functionInstanceObjectOne.calculateQuadratic()
    '''

    ''' 
    Possible Solution (below)
      functionInstanceObjectOne = Quadratic(1, 5, 6)
      output = functionInstanceObjectOne.calculateQuadratic()
      self.assertEqual(output,'The solutions are (-3+0j) and (-2+0j)')
    '''

    # Best Modified Solution (below)
    self.assertEqual(Quadratic(1, 5, 6).calculateQuadratic(),'The solutions are (-3+0j) and (-2+0j)')
    
  def test_case_two(self):
    print("\n\n****Testing correct discriminant calculations...****")
    print("****Choose Option 4 for these tests****\n")

    output = Quadratic(4, 2, 8).calculateQuadratic()
    output1 = Quadratic(1, 4, 7).calculateQuadratic()
    output2 = Quadratic(-5, 4, -98).calculateQuadratic()
    output3 = Quadratic(3, 6, 1).calculateQuadratic()
    output4 = Quadratic(-4, 4, -6).calculateQuadratic()
    # include code here to test whether the function output
    # use assert statements
    # ADD YOUR OWN CODE HERE

  def test_case_three(self): 
    print("\n\n****Testing correct argument types...****")
    print("****Choose Option 1 for these tests****\n")

    output = Quadratic(5, 5, 6).calculateQuadratic()
    output1 = Quadratic(1, 1, 12).calculateQuadratic()
    output2 = Quadratic(3, 2, 3).calculateQuadratic()
    # include code here to test whether the function output
    # use assert statements
    # ADD YOUR OWN CODE HERE

  def test_case_four(self):
    print("\n\nTesting [insert text here]...")
    # ADD YOUR OWN CODE HERE
    pass
