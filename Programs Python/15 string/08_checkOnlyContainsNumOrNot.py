# 8. Write a python script to check if a string contains only numbers.
s = str(input("enter a string"))
flag=0

for i in s:
    if ((i == '0') or (i == '1') or (i == '2')or (i == '3') or (i == '4' ) or( i == '5') or (i == '6' ) or( i == '7' ) or( i == '8' ) or (i == '9')):
        continue
    else:
        flag = 1
        break
if flag == 1:
    print("No")
else:
    print("Yes")
