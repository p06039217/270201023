def password_checker(password):
  password_level = 0
  alpha = ""
  numeric = ""
  specialc = ""
  if " " in password or len(password)<8:
    pass
  else:
    for i in password:
      if i.isnumeric():
        numeric += i
      elif i.isalpha():
        alpha += i
      else:
        specialc += i

  if len(alpha) !=0:
    password_level +=1
  if len(numeric) !=0:
    password_level +=1
  if len(specialc) != 0:
    password_level +=1

  return password_level

password = input("enter the password: ")

print(password_checker(password))
