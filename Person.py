class Person:
  lastIdUsed = 100
  def __init__(self,tmpfName,tmplName):
    self.fName = tmpfName
    self.lName = tmplName
    self.ID = lastIdUsed

p1 = Person("Joe","Jones")

