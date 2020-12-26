
def get_event(n, m = 0):
  if len(n) == 0:
    print(m)
  elif n[-1] % 2 == 0:
    m += 1
    get_event(n[:-1],m)
  else:
    get_event(n[:-1],m) 


get_event([0, 1, 2, 6 ,5 ,3, 4, 5])