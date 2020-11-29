#Write a Python program that takes N integers from user and displays % of even ones.
# Hint: Take N from user at the beginning and use it to create a loop.

numOfnum = int(input("how many numbers?: "))
numOfEvennum = 0
for i in range(numOfnum) : 
  numbers = int(input("please enter the numbers: "))
  if numbers % 2 == 0 :
    numOfEvennum += 1

percent = (numOfEvennum/numOfnum)*100
print(percent,"%")