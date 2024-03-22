j = int(input("Enter any number: "))


flage = 0

for i in range(2,j):
    if (j % i == 0):
        flage = 1
        break

if flage != 1:
    print(j ," is a prime number")
else:
    print(j ," is not a prime number")