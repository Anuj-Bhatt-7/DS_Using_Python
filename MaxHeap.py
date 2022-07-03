def heapify(arr, i):
    size = len(arr)
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < size and arr[largest] < arr[left]:
        largest = left
    if right < size and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest)


def insertNode(arr, key):
    size = len(arr)
    if size == 0:
        arr.append(key)
    else:
        arr.append(key)
        for i in range(size - 1, -1, -1):
            heapify(arr, i)

def deleteNode(arr,value):
    print("After deleting an element: "+str(value))
    size = len(arr)
    i=0
    for i in range(0,size):
        if value == arr[i]:
            break

    arr[i], arr[size-1] = arr[size-1], arr[i]
    arr.remove(value)
    for i in range(size - 1, -1, -1):
        heapify(arr, i)

def displayMaxheap(arr):
    print("Max-heap array: " + str(arr))
    print()


maxList =[]

insertNode(maxList, 9)
insertNode(maxList, 12)
insertNode(maxList, 1)
insertNode(maxList, 20)
insertNode(maxList, 13)
insertNode(maxList, 19)

insertNode(maxList,50)
insertNode(maxList,100)

displayMaxheap(maxList)
deleteNode(maxList,13)
displayMaxheap(maxList)