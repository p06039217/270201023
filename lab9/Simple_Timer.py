def timer(n):
  print(n)   
  if n == 0:
    print("time's up!")
  else:
    import time  
    time.sleep(1)
    timer(n-1)

timer(10)