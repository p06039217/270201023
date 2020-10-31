#Write a Python program to evaluate the following mathematical expression for x=1, y=4, z=0.25
x = 1
y = 4
z = 0.25
math_express = (((2*x+y)**2)*(z**(1/2)))/(x**(1/2)+y**(1/2))
print(math_express)

# or
x = 1
y = 4
z = 0.25
numerator = (((2*x+y)**2)*(z**(1/2)))
denominator = (x**(1/2)+ y**(1/2))
print(numerator/denominator)