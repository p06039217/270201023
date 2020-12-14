a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
def sum():
    sumof = 0
    for i in a_list:
        sumof += i
    return (sumof)**2

print(sum())