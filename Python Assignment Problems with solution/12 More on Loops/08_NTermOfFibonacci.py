# 8. Write a python script to print first N terms of a Fibonacci series
n = (int(input("How many  fib number do u wanna print ")))
a = -1
b = 1
d = 0
while d < n:
    c = a+b
    print(c)
    a = b
    b = c
    d += 1
