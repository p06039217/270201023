def hailstone(n):
  if n == 1:
    print(1)
  elif n % 2 == 0 :
    print(n)
    hailstone(n/2)
  elif n % 2 != 0 :
    print(n)
    hailstone(3*n+1)


hailstone(5)
