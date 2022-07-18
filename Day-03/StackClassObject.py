
def getChoice():
    print("\nMenu Details\n1.PUSH\n2.POP\n3.DISPLAY\n4.EXIT\n")
    choice = int(input("Enter you choice:"))
    return choice

class Stack:
    def __init__(self):
        self.stack = []

    def pushItem(self,item):
        self.stack.append(item)

    def popItem(self):
        item = self.stack[-1]
        del self.stack[-1]
        return item

    def display(self):
        for ele in range(len(self.stack)-1,-1,-1):
            print(self.stack[ele], end=" ")

choice = getChoice()
ob = Stack()
while choice != 4:
    if choice==1:
        item = int(input("Enter value to push: "))
        ob.pushItem(item)
    elif choice==2:
        if len(ob.stack) != 0:
            item = ob.popItem()
            print("Popped value is: ", item)
        else:
            print("Stack UnderFlow")

    elif choice==3:
        if len(ob.stack) != 0:
            ob.display()
        else:
            print("Stack UnderFlow")
    else:
        print("Wrong choice")
    choice = getChoice()
print("Stack Operations are over!")