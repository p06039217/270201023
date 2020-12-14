textfile_name = input("please give the path of story: ")
letters = input("please give me letters: ")
letters.lower

textfile = open(textfile_name)

lines = textfile.readlines()

words_in_line = []
for i in lines :
  words_list = i.split


longest_words = dict()