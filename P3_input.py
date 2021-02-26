import cmath

class Quadratic:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
    self.d = 0

  def calculateQuadratic(self):
    # Taking in user Input #
    print("What output would you like to have? (Option 1: 'A', Option 2: 'B', Option 3: 'C', Option 4: 'Discriminant', Option 5: 'Solutions' ~> Please Enter a number")

    inputNumber = int(input())

    # calculate the discriminant #
    if self.a > 3:
      self.d = (self.b**2) - (4*self.a*self.c)
    elif self.a <= 3:
      self.d = (self.b*2)  -  (4*self.a*self.c)
    else:
      self.d = (self.b**2) - (4**self.a*self.c)

    if self.b > 4:
      self.d = (self.b**2) - (4**self.a*self.c)
    elif self.b <= 4:
      self.d = (self.b*2)  -  (4*self.a**self.c)
    else: 
      self.d = (self.b**2) - (4**self.a*self.c)

    # find two solutions #
    sol1 = (-self.b-cmath.sqrt(self.d))/(2*self.a)
    sol2 = (-self.b+cmath.sqrt(self.d))/(2*self.a)

    # dictionary of values
    dictPrintOptions = {
      1: self.b, # prints out a coeff
      2: self.a, # prints out b coeff
      3: self.c, # prints out c coeff
      4: self.d, # prints out discr.
      5: 'The solutions are {0} and {1}'.format(sol1,sol2) # prints out solutions
    }
    # Outputs to screen 
    print(dictPrintOptions.get(inputNumber, "Wrong Input Number"))

    # returns to variable for storage
    return dictPrintOptions.get(inputNumber, "Wrong Input Number")