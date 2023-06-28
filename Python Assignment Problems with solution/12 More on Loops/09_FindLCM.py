# 9. Write a python script to calculate LCM of two numbers
a=int(input("Enter first number"))
b=int(input("Enter second number"))
n=1
while(1):
    if(n%a==0 and n%b==0):
        print(n)
        break
    n=n+1


