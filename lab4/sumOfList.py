#Write a Python program which calculates sum of the elements of a list.

numOfint = int(input("type the number of integer to be added: "))
listOfint = 0
for i in range(numOfint):
  m = int(input("please enter the numbers in order: "))
  listOfint += m

print(listOfint)
