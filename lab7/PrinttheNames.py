#You’re given a tuple of name and age for everyone in a group. Print out the names of people who are older than 18.
# input = [("Jon",15), ("Ned",45), ("Arya",9), ("Catelyn",44), ("Bran",10)]

names_ages = dict([("Jon",15), ("Ned",45), ("Arya",9), ("Catelyn",44), ("Bran",10)])

for i in names_ages.keys() :
  if names_ages[i] > 18 :
    print(i)

