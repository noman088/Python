# 3. Write a Python script to create a list of first N even natural numbers.


n=int(input("Enter a number"))+1
l=[]
for i in range(1,n,1):
    l.append(2*i)
print(l)



