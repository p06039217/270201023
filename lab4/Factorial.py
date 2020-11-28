#Write a Python program which calculates n factorial where n is given by the user.
number = int(input("throw a integer at me: "))
while number <= 0 :
  print("pleaseee, be the positive..") #if given number is negative
  import time 
  time.sleep(3)
  
  number = int(input("throw a integer at me: "))

else:
  factorial = 1
  for i in range(1, number + 1) :
    factorial *= i
  print(factorial)



  

