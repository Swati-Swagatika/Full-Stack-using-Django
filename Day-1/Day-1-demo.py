#swaaping of two numbers
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# print(num1, num2)
# temp = num1
# num1 = num2
# num2 = temp
# print(num1, num2)

# import math
# s1 = int(input("side1:"))
# s2 = int(input("side2:"))
# s3 = int(input("side3:"))
# s = (s1+s2+s3)//2
# area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
# print(area)

# curr = int(input("Enter current value:"))
# prev = int(input("Enter previous meter value:"))
# if prev >= curr:
#     print("Wrong Info")
# else:
#     unit = curr - prev
#     if unit <= 100:
#         bill = unit * 2.53
#     elif unit <= 200:
#         bill = 100 * 2.53 + (unit-100)*3.75
#     elif unit <= 300:
#         bill = 100 * 2.53 + 100 *3.75 + (unit-200)*4.25
#     else:
#         bill = 100 * 2.53 + 100 * 3.75 + 100 * 4.25 + (unit-300)*8.52
#     print(bill)

# total = int(input())
# for row in range(1,total+1):
#     for col in range(1, row+1):
#         print("*",end="")
#     print()

# total = int(input())
# for row in range(total):
#     for space in range(total-row):
#         print(" ",end="")
#     for col in range(1, row+1):
#         print(chr(col+96),end="")
#         # print("*", end="")
#     for col1 in range(row-1,0,-1):
#         print(chr(col1+96),end="")
#         # print("*",end="")
#     print()


total = int(input())
for row in range(total):
    for space in range(total-row):
        print(" ",end="")
    for col in range(1, row+1):
        print(chr(col+96),end="")
    for col1 in range(row-1,0,-1):
        print(chr(col1+96),end="")
    print()

# print(pow(2,3,3))
# print(bool(""))