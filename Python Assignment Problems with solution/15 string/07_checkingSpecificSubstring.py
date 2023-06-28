# 7. Write a python script to determine whether a string contains a specific substring.
a = str(input("Enter a string"))
b = str(input("enter a substring"))
flag = 0
for i in a:
    if (i == b):
        flag = 1
        print("Yes")
        break
if flag == 0:
    print("Nope")
