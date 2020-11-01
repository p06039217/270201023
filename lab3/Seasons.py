#Write a Python program that reads a month and day from the user. Your program should display the season associated with the date that was entered 
day = float(input("Please, type a day: "))
month = float(input("Please, type a month: "))

what_day_of_year = (month*30)+day
if 365>=what_day_of_year>=1:
   
 if 170>what_day_of_year>=80:
  print("you are in spring season")
 elif 262>what_day_of_year>=170:
  print("you are in summer season")
 elif 351>what_day_of_year>=262:
  print("you are in fall season")
 elif 80>what_day_of_year or 365>=what_day_of_year>=351:
  print("you are in winter season")
  
else:
  print("Please, enter a valid date!")
  
  day = float(input("Please, type a day: "))  #again
  month = float(input("Please, type a month: "))

  if 365>=what_day_of_year>=1:
   
   if 170>what_day_of_year>=80:
     print("you are in spring season")
   elif 262>what_day_of_year>=170:
     print("you are in summer season")
   elif 351>what_day_of_year>=262:
     print("you are in fall season")
   elif 80>what_day_of_year or 365>=what_day_of_year>=351:
     print("you are in winter season")
  