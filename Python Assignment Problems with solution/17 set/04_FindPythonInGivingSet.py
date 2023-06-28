# 4. Write a Python script to find if “Python” is present in the set thisset = {"Java",
# "Python", "Django"}
s = {"Java", "Python", "Django"}
flag = 0
for i in s:
    if i == "Python":
        flag = 1

if flag == 0:
    print("Python is not present")
if flag == 1:
    print("Python is present")
