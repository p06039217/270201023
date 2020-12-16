def is_primes(x):
  for i in range(2,int(x**(1/2))+1):
    if x%i == 0:
      return False
  else:
    return True

def prints_prime_between(x,y):
  for i in range(x,y):
    if is_primes(i) == True:
      print(i)

a = int(input("starting integer: "))
b = int(input("ending integer: "))
prints_prime_between(a,b)







