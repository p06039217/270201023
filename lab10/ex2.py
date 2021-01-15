def hailstone(n):
  print(n)
  if n == 1:
    pass
  elif n % 2 == 0 :
    hailstone(n//2)
  elif n % 2 != 0 :
    hailstone(3*n+1)


hailstone(11)
