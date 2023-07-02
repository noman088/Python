# 2. Write a python script to calculate sum of squares of first N natural numbers

# s = 0
# for i in range(int(input("Enter a number"))):
#     s = s+((i+1)**2)
# print(s)

n=int(input("enter a number"))
s=0
i=1

while i<=n:
    s=s+i*i
    i+=1
print("sum is ",s)
print() #for printing  a next line 



