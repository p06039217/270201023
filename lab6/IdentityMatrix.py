#Write a program that gets a number n and build the identity matrix, then print it. E.g.

identity_matrix = int(input("which number's identity matrix do you want?: "))

matrix_list = []
m = 0

for i in range(identity_matrix) :
    matrix_list.append([0]*identity_matrix)
    matrix_list[m][i] = 1
    m += 1

for i in matrix_list :
    print(i)

