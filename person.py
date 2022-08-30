class Person:
  def __init__(self, data):
    self.age = int(data[0]);
    self.workclass = data[1];
    self.fnlwgt = data[2];
    self.education = data[3];
    self.educationNum = int(data[4]);
    self.maritalStatus = data[5];
    self.occupation = data[6];
    self.relationship = data[7];
    self.race = data[8];
    self.sex = data[9];
    self.capitalGain = data[10];
    self.capitalLoss = data[11];
    self.hoursPerWeek = int(data[12]);
    self.nativeCountry = data[13];
    self.gainClass = data[14];
    
  def __str__(self):
    return str(vars(self))

  def __repr__(self):
    return "{"+str(self.age) + ", " + str(self.nativeCountry) + ", " +str(self.education) + "...}"