# 1.1
# for i in range(3):
#  print("Keeratjot Singh")

# 2.1

# a = 99.5
# b = 23.75
# c = 16.15
# print ("sum of a,b,c is :", a+b+c)

# 2.2
# a = input("Enter first string: ")
# b = input("Enter second string: ")
# c = input("Enter third string: ")

# result = a + b + c

# print("Concatenated String:", result)

# 4.1
# for i in range(1,11):
# print (7," * ", i , " = ", i * 7)

# for i in range(1,11):
#  print (9," * ", i , " = ", i * 9)

# 4.2
# n = int(input("Enter a number: "))
# for i in range (1,11):
# print(n,"*",i,"= ", i*n)
# 4.3
 
# n = int(input("Enter a number: "))

# total = 0

# for i in range(1, n + 1):
#     total = total + i

# print("Sum =", total)

# 5.1
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# maximum = max(a, b, c)

# print("Maximum number is:", maximum)


 # 5.2
# n = int(input("Enter the value of n: "))

# sum = 0

# for i in range(1, n + 1):
#     if i % 7 == 0 and i % 9 == 0:
#         sum = sum + i

# print("Sum =", sum)


# # 5.3
# n = int(input("Enter the value of n: "))

# sum = 0

# for i in range(2, n + 1):
#     prime = True

#     for j in range(2, i):
#         if i % j == 0:
#             prime = False
#             break

#     if prime:
#         sum = sum + i

# print("Sum of prime numbers =", sum)


 # 6.1
# def add_odd(n):
#     total = 0

#     for i in range(1, n + 1):
#         if i % 2 != 0:
#             total = total + i

#     return total


# n = int(input("Enter the value of n: "))

# result = add_odd(n)

# print("Sum of odd numbers =", result)

 # 6.2
# def add_prime(n):
#     total = 0

#     for i in range(2, n + 1):
#         prime = True

#         for j in range(2, i):
#             if i % j == 0:
#                 prime = False
#                 break

#         if prime:
#             total = total + i

#     return total


# n = int(input("Enter the value of n: "))

# result = add_prime(n)

# print("Sum of prime numbers =", result)