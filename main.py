class Advent:
  def __init__(self):
    self.introductionMessage = "Hello Prospective Advent Industries Programming Interns! Attached in this same folder/directory are additional files that should help you with your programming tasks!"
  def __str__(self):
    return self.introductionMessage
if __name__ == "__main__":
  firstInstanceObject = Advent()
  print(firstInstanceObject)