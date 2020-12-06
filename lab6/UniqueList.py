# Write a program that gets a list from the user and shows another list that contains only unique elements of the given list in a descending order.
num_set = set([])
nums = ""
while nums != "quit" :
  nums = input("type an integer (quit to quit): ")
  
  if nums == "quit" :
    break
  else:

    num_set.add(int(nums))

num_list = list(num_set)

num_list.sort()
num_list.reverse()

print(num_list)

