numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]

numbers1_set = set(numbers1)
numbers2_set = set(numbers2)

intersection_set = set()
union_set = set()

for i in numbers1_set :
    for j in numbers2_set :
        if i == j :
            intersection_set.add(i)

print(intersection_set)

for i in numbers1_set :
    union_set.add(i)
for i in numbers2_set :
    if i not in numbers1_set :
        union_set.add(i)
print(union_set)


