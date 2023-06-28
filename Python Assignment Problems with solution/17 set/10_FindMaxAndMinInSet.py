# 10. Write a python program to find the maximum and minimum value in a set.
new_Set = {1, 2, 3, 4, 5, 6}

max = set()
max.add(1)
min = set()
min.add(1)
for i in new_Set:
    if i < i+1:
        max.clear()
        max.add(i)
for i in new_Set:
    if i > i+1:
        min.clear()
        min.add(i)


print(" Max number in new_Set = ", max)
print(" Minimum number in new_Set = ", min)
