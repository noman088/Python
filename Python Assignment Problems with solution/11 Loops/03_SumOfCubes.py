# 3. Write a python script to calculate sum of cubes of first N natural numbers

# s = 0
# for i in range(int(input("Enter a number"))):
#     s = s+((i+1)**3)
# print(s)

n=int(input("enter a number"))
s=0
i=1

while i<=n:
    s=s+i**3
    i+=1
print("sum is ",s)
print() #for printing  a next line 

