def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]


def SelectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if i != min:
            arr[i], arr[min] = arr[min], arr[i]
    
def InsertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

def MergeSort(arr):
    if len(arr)>1:
        mid = (len(arr))//2
        Left = arr[:mid]
        Right = arr[mid:]
        MergeSort(Left)
        MergeSort(Right)

        i = j = k = 0
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                i+=1
            else:
                arr[k] = Right[j]
                j+=1
            k+=1
        
        while i < len(Left):
            arr[k] = Left[i]
            i+=1
            k+=1
        
        while j < len(Right):
            arr[k] = Right[j]
            j+=1
            k+=1

def partition(arr, left, right):
    pivot = arr[right]
    j = left
    for i in range(left, right):
        if pivot >= arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
            j = j+1
    arr[j], arr[right] = arr[right], arr[j]
    return j


def QuickSort(arr, left, right):
    if left < right:
        position = partition(arr, left, right)
        QuickSort(arr, left, position-1)
        QuickSort(arr, position+1, right)

def display(arr):
    for ele in arr:
        print(ele,end=" ")

size = int(input("Enter array size: "))
arr = []
for i in range(size):
    ele = int(input("Enter element: "))
    arr.append(ele)
print("Array before sorting: ")
display(arr)

def getChoice():
    print("\nMENU:\n1.Bubble Sort\n2.Selection Sort\n3.Insertion Sort\n4.Merge sort\n5.Quick Sort\n6.Display\n7.EXIT\n")
    choice = int(input("Enter your Choice: "))
    return choice

choice = getChoice()
while choice!=7:
    if choice == 1:
        BubbleSort(arr)
    elif choice == 2:
        SelectionSort(arr)
    elif choice == 3:
        InsertionSort(arr)
    elif choice == 4:
        MergeSort(arr)
    elif choice == 5:
        QuickSort(arr, 0, size-1)
    elif choice == 6:
        print("\nArray after sorting: \n")
        display(arr) 
    choice = getChoice()