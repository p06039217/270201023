number = int(input("up to what number I check: "))

for i in range(2, number) :
  for divisor in range(2,i) :
    if i % divisor == 0 :
       break
  else:
      print(i)

      