# 8. Write a python script to calculate sum of digits of a given number


# s = 0
# a = str(input("Enter a number"))
# for i in a:
#     s = s+(int(i))
# print(s)
# print()


# s=0
# a=int(input("Enter a number"))
# while a:
#     s=s+a%10
#     a=a//10
# print("sum is : ",s)
# print()


s=sum([int(e) for e in (str(input("Enter a number : ")))])
print(s)


