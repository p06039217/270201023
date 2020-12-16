def binary_to_dec(binary):
  sum = 0 
  valueOfdigit = len(binary)
  for  i in binary:
    if i == "1" :
      sum += 2**(valueOfdigit-1)
      valueOfdigit -= 1
    elif i == "0":
      valueOfdigit -= 1
  return sum

print(binary_to_dec("10010"))


def dec_to_binary(decimal):
  binary = ""
  while decimal != 0 :
    if decimal%2 == 1:
      binary += "1"
    elif decimal%2 == 0:
      binary += "0"
    decimal = decimal//2

  return binary[::-1]

print(dec_to_binary(8))



    





