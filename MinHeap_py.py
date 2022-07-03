def heapify(arr, i):
    size = len(arr)
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < size and arr[smallest] > arr[left]:
        smallest = left
    if right < size and arr[smallest] > arr[right]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, smallest)


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
    flag = 0
    for i in range(0,size):
        if value == arr[i]:
            flag += 1
            break
    if flag == 0:
        print(f"{value} is not present in heap")
        return

    arr[i], arr[size-1] = arr[size-1], arr[i]
    arr.remove(value)
    for i in range(size - 1, -1, -1):
        heapify(arr, i)

def displayMin(arr):
    print("Min-heap array: " + str(arr))
    print()


nodeList = []

insertNode(nodeList, 9)
insertNode(nodeList, 12)
insertNode(nodeList, 1)
insertNode(nodeList, 20)
insertNode(nodeList, 13)
insertNode(nodeList, 19)
insertNode(nodeList,50)
insertNode(nodeList,100)

displayMin(nodeList)
deleteNode(nodeList,13)
displayMin(nodeList)

deleteNode(nodeList,25)
displayMin(nodeList)