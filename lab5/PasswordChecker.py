#Write a Python program that asks the user for a password as soon as he/she enters the right password.
password = "abc123"
passwordEntered = ""

while passwordEntered != password :

  passwordEntered = input("please enter your password: ")
   
  if passwordEntered == "help" :
      print(password[0])

  elif passwordEntered != password :
     print("wrong password. help to 'help'")

print("welcome")