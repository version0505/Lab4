class Person:
  lastIdUsed = 100
  def __init__(self,tmpfName,tmplName):
    self.fName = tmpfName
    self.lName = tmplName
    self.ID = lastIdUsed
  
  def __str__(self):
    tmp = ''
    tmp += self.fName + " " + self.lName + " " + str(self.ID) + "\n"
    return tmp


p1 = Person("Joe","Jones")

