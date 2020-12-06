#Write a program that takes a list of student’s midterm 1, midterm 2 and final exam grades. Then, it calculates and shows each student’s average grade by using the weights 30%, 30% and 40%. Average grades are added into a list. 

numOfstudent = int(input("How many students? "))
exams = []

for i in range(numOfstudent) :
  midterm_1 = int(input("Midterm 1 : "))
  midterm_2 = int(input("Midterm 2 : "))
  final_exam = int(input("Final exam : "))
  
  students_grade = []
  
  students_grade.insert(0,midterm_1)
  students_grade.insert(1,midterm_2)
  students_grade.insert(2,final_exam)
  
  exams.insert(i,students_grade)

print("grades",exams)

averagesOfStudent = []

for i in range(len(exams)) :

   average = exams[i][0]*30/100 + exams[i][1]*30/100 + exams[i][2]*40/100

   averagesOfStudent.append(average)


print("the averages",averagesOfStudent)



aa_students = []

for i in averagesOfStudent :
  if i >=90 :
       aa_students.append(i)

print("AA Students", aa_students)

   





