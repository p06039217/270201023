
def sumOflist(n):
  if len(n) == 0:
    return 0
  if isinstance(n[0],list):
    return n[0] + sumOflist(n[1:])
  else:
    return n[0] + sumOflist(n[1:])

print(sumOflist([1,2,3,4]))




