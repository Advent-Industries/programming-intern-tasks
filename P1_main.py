
class Manipulation:
  def __init__(self):
    self.title = "Submersible System Data Transmission and Manipulation"
    self.reminder = "Remember to edit the values in the following dictionaries when you are updating the system values after decoding the encrypted transmissions! You may add or remove functions, parameters and arguments for methods, or organization as you would like to. Do NOT edit anything within this __init__ method."
    self.author, self.designer = 'Silas John', 'Alden Wang'
    self.systemInformationAnalog = {
      "propellors": [0, 99],
      "motors": [69, 50],
      "pH": '7pH',
      "speed": 0,
      "waterTemp": "89C",
      "mastConfig": 76,
      "pressureSens": 1,
      "sonarSens": 0,
      "battery": "100", 
      "depth": '30m',
      "lightBut": 0, 
      "vidQuality": 720
    }
    self.systemInformationDigital = {
      "rfMaster": 1,
      "limitSwitch": [0, 0, 0],
      "hitOrMiss": 'MIS',
      "videoTransmit": 1
    }
  
  def outputSummary(self):
    # insert code to form your first and last output summary of the system here
    #
    # you should have the same code forming an output summary before and after 
    # system changes
    #
    # String Formatting is really useful in situations like this
    pass

  def openFile(self):
    pass
    # insert code to open and read file contents

  def outputUPDATES(self):
    # insert code for your outputting updates to the system
    pass
  
  def decodeEncryption(self):
    # insert code to decode the transmission and update the system variables in the
    # dictionaries found above
    # Maybe every time you decode a transmission, you can call outputUPDATES() here to instantly announce the update to the system?
    pass

  def masterManipulator(self):
    self.outputSummary()
    self.decodeEncryption()
    self.outputSummary()