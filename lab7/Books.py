# Define the list books at the beginning. 
# books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]

books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
books_dict = {}

for i in books :
  books_dict[i] = (len(i), len(set(i)))

for i in books_dict.keys() :
  print(i,"-->",books_dict[i])


  #update 

  for i in books_dict.keys()
