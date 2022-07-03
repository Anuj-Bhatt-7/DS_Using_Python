class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackList:
    def __init__(self):
        self.top = 0

    def pushElement(self, key):
        new_node = Node(key)
        new_node.next = self.top
        self.top = new_node

    def popElement(self):
        temp = self.top
        if self.top == 0:
            print("Underflow!")
        else:
            print(f"popElement element is: {self.top.data}")
            self.top = self.top.next
            del temp

    def peak(self):
        if self.top == 0:
            print("Underflow!")
        else:
            print(f"Peek element is: {self.top.data} ")

    def displayStack(self):
        if self.top == 0:
            print("Underflow!")
        else:
            print("Element in stack: ")
            temp = self.top
            while temp != 0:
                print(temp.data)
                temp = temp.next


stack = StackList()
stack.pushElement(34)
stack.pushElement(14)
stack.pushElement(89)
stack.pushElement(50)
stack.pushElement(79)
stack.displayStack()

stack.popElement()
stack.displayStack()

stack.peak()
