#Write a Python code to ask user to enter two values: one for GPA and the other for Number of Lectures. According to the below table, decide whether user will be graduated or not. If not, give an appropriate message as given table.
gpa = float(input("Please type your GPA: "))
numberOflectures = float(input("Please type number of lecture: "))
if 2.0>gpa and 47>numberOflectures:
  print("not enough number of lectures and GPA") 
elif gpa>=2.0 and 47>numberOflectures:
  print("not enough number of lectures")
elif gpa<2.0 and numberOflectures>=47:
  print("not enough GPA")
else:
  print("GRADUATED!!")