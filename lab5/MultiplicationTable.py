#Write a Python program that takes an integer from user and displays the multiplication table for it. 

number = int(input("type a integer: "))

for i in range(1,11):
  print(number,"x",i,"=",number*i)
  
