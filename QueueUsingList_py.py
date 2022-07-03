class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0

    def enqueueElement(self, key):
        new_node = Node(key)
        new_node.next = None
        if self.front == 0 and self.rear == 0:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeueElement(self):
        if self.front == 0 and self.rear == 0:
            print("Underflow!")
        elif self.front == self.rear:
            print(f"dequeueElement element is: {self.front.data}")
            self.front = self.rear = 0

        else:
            print(f"dequeueElement element is: {self.front.data}")
            self.front = self.front.next

    def peek(self):
        if self.front == 0 and self.rear == 0:
            print("Underflow!")
        else:
            print(f"Peek element is: {self.front.data}")

    def displayQueue(self):
        temp = self.front
        if self.front == 0 and self.rear == 0:
            print("Underflow!")
        else:
            print("Element is queue: ", end=" ")
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()


queue = Queue()
queue.enqueueElement(34)
queue.enqueueElement(64)
queue.enqueueElement(94)
queue.enqueueElement(14)
queue.displayQueue()
queue.dequeueElement()
queue.displayQueue()
queue.peek()
