# 8. Write a python program to Sort a tuple of tuples by the second item.
# tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
# t = (('a', 21), ('b', 37), ('c', 11), ('d', 29))
# t2 = sorted(t)
# print(t2)


t= (('a', 21),('b', 37),('c', 11), ('d',29))
l1=list(t)
l2=l1.sort(key=lambda item:item[1])# I don't know how this works I just copied from another's repo.
print(l1)
# print(l2) 