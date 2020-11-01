#Write a Python code that asks the user for parameters(a, b, c) of a quadratic equation represented as: ax2 + bx + c. The code should calculate & print out the roots accordingly. 
# Discriminant: 
#− When Δ>0, there are two real roots 
#− When Δ=0, there is one real root 
#− When Δ<0, there are two complex roots
print("ax^2 + bx + c")
a = float(input("Please, enter the number representing a : "))
b = float(input("Please, enter the number representing b : "))
c = float(input("Please, enter the number representing c : "))
discriminant = b**2-(4*a*c)
if discriminant>0:
  print("there are two real roots")
elif discriminant==0:
  print("there is one real root")
else:
  print("there are two complex root")