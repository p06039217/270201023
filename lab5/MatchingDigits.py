#Write a Python program that asks the user for two positive integers and finds the number of matching digits (starting from units digit).
num1 = list(input("enter a positive integer: "))
num2 = list(input("enter a positive integer: "))

num1.reverse()
num2.reverse()

samedig_Num = 0

num2_index = 0

for i in num1:
  if i == num2[num2_index] :
    samedig_Num += 1
    num2_index += 1

print(samedig_Num)

