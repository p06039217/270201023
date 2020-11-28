#Write a Python program that asks the user for a year and then it checks whether the entered year is a leap year or not. Note: Leap years are "exactly divisible" by 4 but century years which are not divisible by 400 are not leap years. Examples: 100, 1900, 2017 → not leap years 4, 400, 1992, 2000 → leap years

year = int(input("type a year: "))

if year % 4 == 0 :
  if year % 100 == 0 :
    if year % 400 == 0 :
      print("a leap year")
    else:
      print("not a leap year")
  else: 
    print("a leap year")  


else:
  print("not a leap year")

    
