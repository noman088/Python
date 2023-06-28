# 5. Write a python program to check if all items in the tuple are the same.
t = (1, 1, 1, 1, 1)
flag = 0
for i in t:
    if t[i] != t[i+1]:
        flag = 1
        break
if flag == 0:
    print("same")
if flag == 1:
    print("Not same")
