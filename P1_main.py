
class Manipulation:
  def __init__(self):
    self.title = "Submersible System Data Transmission and Manipulation"
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

  