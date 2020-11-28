#Write a Python program that asks the user for two integers a and b and calculates ab without using ** operator and pow function.

a = int(input("type a integer: "))
b = int(input("type a integer: "))
c = 1
if b >= 0:
  for i in range(b): 
    c *= a
elif b < 0 :
    for i in range(b, 0) :
      c /= a

print(c)