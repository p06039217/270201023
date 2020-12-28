def multip(n,m=3):
  if m == 1:
    return n
  
  m -=1
  
  return n + multip(n,m)



print(multip(6))


