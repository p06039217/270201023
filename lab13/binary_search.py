def binary_search(alist, x):
  if len(alist) == 0:
    return -1

  mid = len(alist)//2
  item = alist[mid]
  if item == x:
    return mid
  elif x < item:
    return binary_search(alist[:mid],x)
  else:
    loc = binary_search(alist[mid+1:],x)
    if loc == -1:
      return -1
    else:
      return mid + loc + 1

nums = [0,2,3,4,7,9,12,15,33,66,78,92]

print(binary_search(nums,33))
  