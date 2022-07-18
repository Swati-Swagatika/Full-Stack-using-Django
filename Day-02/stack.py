# stack = []
# def getChoice():
#     print("\nMenu Details\n1.PUSH\n2.POP\n3.DISPLAY\n4.EXIT\n")
#     choice = int(input("Enter you choice:"))
#     return choice

# def pushItem(item):
#     stack.append(item)

# def popItem():
#     item = stack[-1]
#     del stack[-1]
#     return item

# def display():
#     for ele in range(len(stack)-1,-1,-1):
#         print(stack[ele], end=" ")

# choice = getChoice()
# while choice != 4:
#     if choice==1:
#         item = int(input("Enter value to push: "))
#         pushItem(item)
#     elif choice==2:
#         if len(stack) != 0:
#             item = popItem()
#             print("Popped value is: ", item)
#         else:
#             print("Stack UnderFlow")

#     elif choice==3:
#         if len(stack) != 0:
#             display()
#         else:
#             print("Stack UnderFlow")
#     else:
#         print("Wrong choice")
#     choice = getChoice()