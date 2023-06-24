# 9. Write a Python script to create a list of city names taken from the user.

l = []
for i in range(int(input("How many city"))):
    if (i == 0):
        print("Enter city names : ")
    l.append(str(input()))
    i += 1
print(l)
