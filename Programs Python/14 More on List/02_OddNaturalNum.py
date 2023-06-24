# 2. Write a Python script to create a list of first N odd natural numbers.

l1=[]
n=int(input("Enter a number"))+1
for i in range(1,n,1):
    l1.append(2*i-1)
print(l1)