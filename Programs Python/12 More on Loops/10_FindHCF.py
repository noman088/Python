# 10. Write a python script to calculate HCF of two numbers
n = int(input("Enter first Number"))
m = int(input("Enter second Number"))
a = max(n, m)
for i in range(2, a//2, 1):
    if (m % i == 0 and n % i == 0):
        HCF = i
print(HCF)
