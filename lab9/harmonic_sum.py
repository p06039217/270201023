def harmonic(n):
  if n == 0 or n == 1:
    return n
  else:
    return 1/n + harmonic(n-1)

print(harmonic(2))