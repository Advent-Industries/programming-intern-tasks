import cmath

class Quadratic:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
    self.d = 0

  def calculateQuadratic(self):
    
    print("What output would you like to have? (Option 1: 'A', Option 2: 'B', Option 3: 'C', Option 4: 'Discriminant', Option 5: 'Solutions' ~> Please Enter a number")

    inputNumber = int(input())

    # calculate the discriminant
    self.d = (self.b**2) - (4*self.a*self.c)

    # find two solutions
    sol1 = (-self.b-cmath.sqrt(self.d))/(2*self.a)
    sol2 = (-self.b+cmath.sqrt(self.d))/(2*self.a)

    dictPrintOptions = {
      1: self.a,
      2: self.b,
      3: self.c,
      4: self.d,
      5: 'The solutions are {0} and {1}'.format(sol1,sol2)
    }
    print(dictPrintOptions.get(inputNumber, "Wrong Input Number"))

    ''''
    switch(inputNumber):
      case 1:
        return self.a
        break

      case 2:
        return self.b
        break

      case 3:
        return self.c
        break

      case 4:
        return self.d
        break
        
      case 5: 
        # f'The solutions are {sol1} and {sol2}' 
        print('The solutions are {0} and {1}'.format(sol1,sol2))
        break


if __name__ == "__P3_input__":
  functionInstanceObject = Quadratic()
'''