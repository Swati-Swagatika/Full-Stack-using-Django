#LINEAR SEARCH
# n = int(input())
# arr = list(map(int, input().split()))
# ele = int(input())
# ans = 0
# for i in range(len(arr)):
#     if arr[i] == ele:
#         ans = i
# if ans == 0:
#     print("not present")
# else:
#     print("present at: ",ans)

#BINARY SEARCH
# def binarySearch(arr, low, high, ele):
#     while low <= high:
#         mid = (low+high)//2
#         if arr[mid]==ele:
#             return mid
#         elif arr[mid] < ele:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1

# n = int(input())
# arr = []
# for i in range(n):
#     x = int(input("Enter an element: "))
#     arr.append(x)
# ele = int(input())
# position = binarySearch(arr, 0, n-1, ele)
# if position == -1:
#     print("Element is not found")
# else:
#     print("Element found at: ", position)

#SELECTION SORT
# def printList(arr):
#     for i in range(len(arr)):
#         print(arr[i], end=" ")
# def selectionSort(arr):
#     for i in range(len(arr)-1):
#         min = i
#         for j in range(i+1,len(arr)):
#             if arr[j] < arr[min]:
#                 min = j
#         if i!=min:
#             arr[i], arr[min] = arr[min], arr[i]
        

# n = int(input())
# arr = []
# for i in range(n):
#     x = int(input("Enter an element: "))
#     arr.append(x)
# print("Before Sorting: ")
# printList(arr)
# selectionSort(arr)
# print()
# print("After Sorting")
# printList(arr)

#QUICK SORT

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

def partition(arr, start, end):
    pivot = arr[end]
    j = start
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j+=1
    arr[j],arr[end] = arr[end],arr[j]
    return j

def quickSort(arr, start, end):
    if start < end:
        position = partition(arr, start,end)
        quickSort(arr, start,position-1)
        quickSort(arr,position+1,end)
        
n = int(input())
arr = []
for i in range(n):
    x = int(input("Enter an element: "))
    arr.append(x)
print("Before Sorting: ")
printList(arr)
quickSort(arr,0,n-1)
print()
print("After Sorting")
printList(arr)
