#Ask for an email address.Check if this email address is ceng113@example.com 
#Assume that (for this domain): Email addresses are case-insensitive 	(e.g. abc@def.com and ABC@DEF.com are the same address)
#Dots before @ sign are ignored	(e.g. a.b.c@def.com and abc@def.com are the same address)

email_corrert = list("ceng113@example.com")


email = input("please type your email: ")

email_1 = email.lower()
email_1 = list(email_1)



while email_1[:email_1.index("@")].count(".") > 0:
    email_1.remove(".")


if email_corrert == email_1 :
  print("welcome !")

else:
  print("wrong password! keep your eyes on the keyboard while typing.")



  

















