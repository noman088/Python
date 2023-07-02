# 6. Write a python script to calculate factorial of a given number

# fact = 1
# for i in range(int(input("Enter a number"))):
#     fact = fact*(i+1)
# print(fact)

n=int(input("Enter a number : "))
p,i=1,1
while i<=n:
    p=p*i
    i+=1
print("Factorial is ",p)
print()
