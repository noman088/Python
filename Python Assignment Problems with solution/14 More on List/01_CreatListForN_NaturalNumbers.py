# 1. Write a Python script to create a list of first N natural numbers.
l1=[]
n=int(input("Enter a number"))+1
for a in range(1,n,1):
     l1.append(a)
print(l1)