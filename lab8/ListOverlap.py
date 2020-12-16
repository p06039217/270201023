def get_rand_list(b,e,N):
  import random
  list_random = []
  for i in range(N):
    list_random.append(random.randint(b,e))

  return list_random

def get_overlap():
  overlap = []
  list1= []
  list2= []
  list3= []
  for i in get_rand_list(0,10,5):
    list1.append(i)
  for i in get_rand_list(0,10,5):
    list2.append(i)
    list3.append(i)
  for i in list1:
    if i in list2:
      overlap.append(i)
      list2.remove(i)
      continue
  return list1,list3,overlap

print(get_overlap())

print("-"*20,"second way","-"*20)  # second way


def get_overlap():
  overlap = []
  list1= []
  list2= []
  for i in get_rand_list(0,10,5):
    list1.append(i)
  for i in get_rand_list(0,10,5):
    list2.append(i)
  for i in set(list1):
    if list1.count(i) != 0 and list2.count(i) !=0:
      if list1.count(i) == list2.count(i):
        for j in range(list1.count(i)):
          overlap.append(i)
      elif list1.count(i) > list2.count(i):
        for j in range(list2.count(i)):
          overlap.append(i)
      elif list1.count(i) < list2.count(i):
        for j in range(list1.count(i)):
          overlap.append(i)
  
  return list1,list2,overlap

print(get_overlap())
  

 




  