start = int(input("Enter the starting range: "))
end = int (input("Enter the end range: "))
print("prime numbers in the range" , start, "to " , end)

for i in range(start, end + 1):
    flag = 0
    for j in range(2,i):
        if (i % j == 0):
            flag = 15
            break
    if (flag == 0):
        print (i, end = ' , ')


# it is another menthod to find prime or not

# j = int(input("Enter any number: "))


# flage = 0

# for i in range(2,j):
#     if (j % i == 0):
#         flage = 1
#         break

# if flage != 1:
#     print(j ," is a prime number")
# else:
#     print(j ," is not a prime number")