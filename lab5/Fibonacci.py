#Write a Python program that asks the user how many Fibonacci numbers to generate and then displays them.

howmanyFibo = int(input("How many Fibonacci do u want? "))

listOffibo = [1,1]

if howmanyFibo == 1 :
  print(1)

elif howmanyFibo == 0 :
  print("nothingg")
  

elif howmanyFibo >=2 :
  for i in range(1, howmanyFibo-1) :
    lastnumber1 = listOffibo[len(listOffibo)-1]
    lastnumber2 = listOffibo[len(listOffibo)-2]

    newnumber = lastnumber1 + lastnumber2
  
  
    listOffibo.append(newnumber)

  print(listOffibo)






