#1. swap the values of two variables without using a third variable.
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# print(num1, num2)
# num1, num2 = num2, num1
# print(num1, num2)

#2. area of a triangle by inputting the three sides. 
# import math
# s1 = int(input("side1:"))
# s2 = int(input("side2:"))
# s3 = int(input("side3:"))
# s = (s1+s2+s3)//2
# area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
# print(area)

#3. enter the two sides of a rectangle and calculate the radius of the circle whose area is same as the rectangle.
# import math
# l = int(input("length of rectangle: "))
# b = int(input("breadth of rectangle: "))
# area = l*b
# r = math.sqrt(area/math.pi)
# print(r)

#4. calculate the gross salary of an employee by giving basic salary. Also calculate DA (60%) HRA(15%), Conveyance (15%), Medical (10%),Tax(5%).
# basicSalary = int(input("Enter the basic salary: "))
# DA = 0.6*basicSalary
# HRA = 0.15*basicSalary
# Conveyance = 0.15*basicSalary
# medical = 0.1*basicSalary
# tax = 0.05*basicSalary
# GrossSalary = basicSalary + DA + Conveyance + medical - tax
# print('DA: ', DA )
# print('HRA: ', HRA)
# print('Conveyance: ', Conveyance)
# print('Medical: ',medical)
# print('tax: ', tax)
# print('Gross Salary: ', GrossSalary)

#5. smallest between three numbers using conditional operator
# a = int(input('Enter first number  : '))
# b = int(input('Enter second number : '))
# c = int(input('Enter third number  : '))
# smallest = 0
# if a < b and a < c :
#     smallest = a
# if b < a and b < c :
#     smallest = b
# if c < a and c < b :
#     smallest = c
# print("Smallest: ",smallest)

#6. evaluate the expression from inputted values of a, b, c, d. x = (a - b) / (c - d)
# a = int(input("Enter num1: "))
# b = int(input("Enter num2: "))
# c = int(input("Enter num3: "))
# d = int(input("Enter num4: "))
# if c - d == 0:
#     print("Error")
# else:
#     x = (a-b)/(c-d)
#     print(x)

#7. compute the real roots of the quadratic equation ax2 +bx+c=0. 
# from math import sqrt
# a = int(input("Enter coefficient1: "))
# b = int(input("Enter coefficient2: "))
# c = int(input("Enter constant: "))
# r = (b**2) - (4*a*c)
# if a==0 and b==0:
#     print("No Solution")
# elif a==0 and b!=0:
#     x = (-b)/2*a
#     print("Only one real root: %f" %x)
# elif r==0:
#     x1 = x2 = (-b)/2*a
#     img = sqrt(-(r))/2*a
#     print("Complex roots: ")
#     print("root1: %f+%f, root2: %f-%f"%(x1,img,x2,img))
# else:
#     x1=(-b + sqrt(r)/(2*a))
#     x2=(-b - sqrt(r)/(2*a))
#     print("Two real roots are: %f, %f"%(x1, x2))

#8. Calculate the grade of the student according to the average mark
# subject1=int(input("Enter marks of 1st subject: "))
# subject2=int(input("Enter marks of 2nd subject: "))
# subject3=int(input("Enter marks of 3rd subject: "))
# average = (subject1+subject2+subject3)/3
# if average >= 90:
#     print("GRADE: 0")
# elif average >=80:
#     print("GRADE: E")
# elif average >= 70:
#     print("GRADE: A")
# elif average >= 60:
#     print("GRADE: B")
# elif average >= 50:
#     print("GRADE: C")
# elif average >= 40:
#     print("GRADE: D")
# else:
#     print("GRADE: F")

#9. Calculate the electric bill
# curr = int(input("Enter current value:"))
# prev = int(input("Enter previous meter value:"))
# if prev >= curr:
#     print("Wrong Info")
# else:
#     unit = curr - prev
#     if unit <= 100:
#         bill = unit * 2.40
#         print(bill)
#     elif unit <= 200:
#         bill = (100 * 2.40 )+ (unit-100) * 3.50
#         print(bill)
#     else:
#         bill = (100 * 2.40) + (100 * 3.50) + (unit-200) * 4.20
#         print(bill)

#10. round a given floating point number to integer by considering the floor & ceiling operation without using built in function. Also re write the same program using 
# import math
# num = float(input("Enter a floating number: "))
# print("WITHOUT BUILTIN FUNCTION")
# if num > 0:
#     num1 = str(num)
#     s = num1.find('.')
#     print("CEILING: %d"%(int(num1[0:s])+1))
#     print("FLOORING: %d"%int(num1[0:s]))
# else:
#     num1 = str(num)
#     s = num1.find('.')
#     print("CEILING: %d"%int(num1[0:s]))
#     print("FLOORING: %d"%(int(num1[0:s])-1))

# print("WITH BUILTIN FUNCTION")
# print("CEILING: ", math.ceil(num))
# print("FLOORING: ",math.floor(num))

#11. GCD and LCM
# a = int(input("Enter number1: "))
# b = int(input("Enter number2: "))
# if a>b:
#     greater = a
# else:
#     greater = b
# while(True):
#     if greater % a == 0 and greater % b ==0:
#         lcm = greater
#         break
#     greater += 1

# print("LCM: ", lcm )

# gcd = (a*b)/lcm

# print("GCD: ", gcd)

#12. largest and smallest of n numbers
# n = int(input("Enter value n: "))
# arr = list(map(int, input().split()))
# print("largest: ", max(arr))
# print("smallest: ",min(arr))

#13. decimal to binary
# def DecimalToBinary(num):
#     if num >= 1:
#         DecimalToBinary(num // 2)
#     print(num % 2, end = '')
# num = int(input("Enter a number: "))
# DecimalToBinary(num)


#14.
# num = input("Enter number: ")
# for digit in  num:
#     if digit == '0':
#         print("Zero ", end = " ")

#     elif digit == '8':
#         print("Eight", end = " ")
    
#     elif digit == '9':
#         print("Nine ", end = " ")
#     elif digit == '1':
#         print("One ", end = " ")

#     elif digit == '2':
#         print("Two ", end = " ")

#     elif digit=='3':
#         print("Three",end=" ")

#     elif digit == '4':
#         print("Four ", end = " ")

#     elif digit == '5':
#         print("Five ", end = " ")

#     elif digit == '6':
#         print("Six ", end = " ")

#     elif digit == '7':
#         print("Seven", end = " ")
    
#15.
total = int(input())
for row in range(total):
    for space in range(total-row):
        print(" ",end=" ")
    for col in range(1, row+1):
        print(chr(col+96),end=" ")
    for col1 in range(row-1,0,-1):
        print(chr(col1+96),end=" ")
    print()