#● Write a Python program that determines and
#prints whether a password is valid or not.
#● A valid password is at least 8 characters long
#and contains at least one uppercase letter
#(A-Z), at least one lowercase letter (a-z),
#and at least one number (0-9).

password = str(input("enter the password: "))

upper = 0
lower = 0
digit = 0


for i in password :
    if len(password) >=8 :
      if i.isdigit() :
          digit += 1

      if i.isupper() :
          upper += 1
      if i.islower() :
          lower += 1
            

if len(password) < 8 or upper == 0 or lower == 0 or digit == 0:
    print("not valid !")
else :
    print("ok. its valid.")

