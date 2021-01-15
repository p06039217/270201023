class  Employee:
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary

  def getName(self):
    return self.name

  def setName(self,name):
    self.name = name

  def getSalary(self):
    return self.salary
  
  def setSalary(self,salary):
    if salary >= 0:
      self.salary = salary

  def allInfo(self):
    print(f"Name: {self.name} \nSalary: {self.salary}" )


class Company:
  def __init__(self):
    self.employee_list = []

  def getList(self):
    return self.employee_list

  def setList(self,employee_list):
    self.employee_list = employee_list

  def addList(self,new_employee):
    if isinstance(new_employee,Employee):
      self.employee_list.append(new_employee)

  def averageSalary(self):
    salary = 0
    for i in self.employee_list:
      salary += i.getSalary()

    return salary/len(self.employee_list)
  
  def allEmployee(self):
    for i in self.employee_list:
      i.allInfo()

  
  
  
c = Company()
e1 = Employee("One", 10)
e2 = Employee("Two", 20)
e3 = Employee("Three", 30)

c.addList(e1)
c.addList(e2)
c.addList(e3)
c.addList(90)
c.allEmployee()


      


  