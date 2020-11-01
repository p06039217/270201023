#Write a Python code that asks the user for three numbers, calculate the minimum of them and print it.
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))
if y>=x and z>=x :
  print(x)
elif z>=y:
  print(y)
else:
  print(z)

