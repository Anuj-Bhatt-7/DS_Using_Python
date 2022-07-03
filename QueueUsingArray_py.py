class Queue:
    ele = []
    front = rear = -1

    def enqueueElement(self, data):
        if self.rear == -1 and self.front == -1:
            self.rear = self.front = 0
            self.ele.append(data)
        else:
            self.rear += 1
            self.ele.append(data)

    def dequeueElement(self):
        if self.front == -1 and self.rear == -1:
            print("Underflow!")
        else:
            print(f"Dequeued element is : {self.ele[self.front]}")
            self.front += 1

    def peek(self):
        if self.front == -1 and self.rear == -1:
            print("Underflow!")
        else:
            print(f"Peek element is: {self.ele[self.front]}")

    def displayQueue(self):
        temp = self.front
        if self.front == -1 and self.rear == -1:
            print("Underflow!")
        else:
            while temp <= self.rear:
                print(self.ele[temp], end=" ")
                temp = temp + 1
            print()


queue = Queue()
print("Element in queue")
queue.enqueueElement(34)
queue.enqueueElement(14)
queue.enqueueElement(54)
queue.displayQueue()

queue.dequeueElement()
queue.displayQueue()
queue.peek()
