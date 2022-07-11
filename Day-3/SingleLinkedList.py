class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

#Define LinkedList
class LinkedList:
    def __init__(self):
        self.start = None
        self.size = 0
    
    def traversal(self):
        if self.start == None:
            print("List is empty")
        else:
            tempnode = self.start
            while (tempnode != None):
                print(tempnode.data, end=" ")
                tempnode = tempnode.next
    
    #Insert at the beginning of the linkedList
    def insertBegin(self, item):
        newnode = Node(item) #Create node
        self.size = self.size + 1
        if self.start == None:
            self.start = newnode
        else:
            newnode.next = self.start
            self.start = newnode

    #Delete at the beginning of the linkedList
    def deleteBegin(self):
        if self.start == None:
            print("List is empty")
        else:
            tempnode = self.start
            self.size = self.size - 1
            if self.start.next == None:
                self.start = None
            else:
                self.start = tempnode.next
            print("Deleted node is: ", tempnode.data)
            del tempnode
    
    #Insert at the end of the Linkedlist
    def insertEnd(self, item):
        newnode = Node(item)
        temp = self.start
        self.size = self.size + 1
        if self.start == None:
            self.start = newnode
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = newnode

    #Delete at the end of the LinkedList
    def deleteEnd(self):
        if self.start == None:
            print("List is empty")
        else:
            temp = self.start
            prev = temp
            self.size = self.size - 1
            while temp.next!=None:
                prev = temp
                temp = temp.next 
            prev.next = None
            print("Deleted node is: ", temp.data)
            del temp

    #Insert after a node in the LinkedList
    def insertAfter(self,item, nodeAfter):
        newnode = Node(item)
        if self.start == None:
            self.start = newnode
        else:
            temp = self.start
            prev = temp
            self.size = self.size + 1
            while temp.data != nodeAfter:
                prev = temp
                temp = temp.next
            newnode.next = prev.next
            prev.next = newnode

    #Delete after a node in the LinkedList
    def deleteAfter(self, node):
        if self.start == None:
            print("List is empty")
        else:
            temp = self.start
            while temp.data != node:
                temp = temp.next
                if temp == None:
                    print("Node not found")
                    return
            last = temp.next
            if last == None:
                print(node," is the last node.")
            else:
                self.size = self.size - 1
                print(last.data," is deleted")
                temp.next = last.next
                del last

    #Insert at a specific position in the LinkedList
    def insertAtPosition(self, item, position):
        temp = self.start
        counter = 1
        self.size = self.size + 1
        newnode = Node(item)
        while temp.next != None:
            if counter == position:
                newnode.next = temp.next
                temp.next = newnode
            counter += 1
            temp = temp.next

    #Delete at a specific position  in the LinkedList
    def deleteAtPosition(self, position):
        temp = self.start
        prev = temp
        counter = 1
        self.size = self.size - 1
        while temp.next != None:
            if counter == position:
                prev.next = temp.next
                break
            counter += 1
            prev = temp
            temp = temp.next
        print("Node Deleted successfully!")
        del temp

    #Reverse a LinkedList
    def reverse(self):
        prev = None
        curr = self.start
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.start = prev

    #Sorting a LinkedList   
    def sortLinkedList(self):
        prev = self.start
        curr = None
        if self.start == None:
            return
        else:
            while prev != None:
                curr = prev.next
                while curr!=None:
                    if prev.data > curr.data:
                        prev.data, curr.data = curr.data, prev.data
                    curr = curr.next
                prev = prev.next
                

    def totalNodes(self):
        if self.size == 0:
            print("List is empty and zero number of nodes")
        else:
            print("Total: ",self.size," number of nodes.")


def getChoice():
    print("\nMenu Details\n1.Traversal\n2.Total Nodes\n3.Insert at Beginning\n4.Delete at Beginning\n5.Insert at end\n6.Delete at end\n7.Insert after a given node\n8.Delete after a given node\n9.Insert at a specific position\n10.Delete at a specific position\n11.Reverse LinkedList\n12.Sort LinkedList\n13.EXIT\n")
    choice = int(input("Enter you choice:"))
    return choice

#main function:
choice = getChoice()
#object of linkedList class
ob = LinkedList()
while choice != 13:
    if choice == 1:
        ob.traversal()
    elif choice == 2:
        ob.totalNodes()
    elif choice == 3:
        item = int(input("Enter Value to Insert: "))
        ob.insertBegin(item)
    elif choice == 4:
        ob.deleteBegin()
    elif choice == 5:
        item = int(input("Enter value to insert: "))
        ob.insertEnd(item)
    elif choice == 6:
        ob.deleteEnd()
    elif choice == 7:
        item = int(input("Enter value to insert: "))
        position = int(input("Enter after which node you want to insert: "))
        ob.insertAfter(item, position)
    elif choice == 8:
        node = int(input("Enter node after which you want to delete: "))
        ob.deleteAfter(node)
    elif choice == 9:
        item = int(input("Enter value to insert: "))
        position = int(input("Position where you want to insert: "))
        ob.insertAtPosition(item,position)
    elif choice == 10:
        position = int(input("Position where you want to delete: "))
        ob.deleteAtPosition(position)
    elif choice == 11:
        ob.reverse()
    elif choice == 12:
        ob.sortLinkedList()
    else:
        print("Wrong choice")
    choice = getChoice()
print("LinkedList operations are over!")