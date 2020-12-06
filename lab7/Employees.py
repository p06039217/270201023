#Assume that there is a company with 5 employees. ● Take each employee’s name and salary from the user, and store them in a dictionary “employees”. ● Print the names of the employees with the highest three salaries.

employees = {}

for i in range(5) :
  name = input("Empployee's name: ")
  salary = int(input("Employee's salary: "))
  employees[name] = salary

print(employees)


highest_salaries = {}
m = "mehmet"
employees_tuple = tuple(employees.items())
while   m == "mehmet" :
  for x,y in employees_tuple :
    if y == max(employees.values()) :
      highest_salaries[x] = y
      del employees[x]

    
  if len(highest_salaries.items()) == 3 :
    break


print(highest_salaries)
  
# the code works correctly on pycharm but but repl.it  generates errors