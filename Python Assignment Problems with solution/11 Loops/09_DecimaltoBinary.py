# 9. Write a python script to print binary equivalent of a given decimal number. (do not
# use bin() method)


### 1st method
# a=int(input("Enter a number"))
# n=[]
# while a>0:
#     digit =(a%2)
#     n.append(digit)
#     a//=2
# n.reverse();
# for e in n:
#     print(e,end='')
    

# 2nd Method
n=int(input("Enter a number"))
s=''
while n:
    # s=s+str(n%2)/// this will give reverse 
    s=str(n%2)+s
    n=n//2
print(s)
print()


