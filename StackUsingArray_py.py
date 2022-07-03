class Stack:
    item = []
    top=-1

    def __init__(self):
        self.item = []
        self.top = -1

    def pushelement(self,element):
        self.top = self.top +1
        self.item.append(element)

    def popElement(self):
        if(self.top==-1):
            print("Underflow")
        else:
            self.item.popElement()
            self.top = self.top - 1
            print("Last item has been popElementped from the stack")

    def peekElement(self):
        if (self.top == -1):
            print("Stack is empty")
        else:
            print(self.item[len(self.item) - 1])

    def displayStack(self):
        if (self.top == -1):
            print("Stack is empty")
        else:
            for i in self.item:
                print(i,end=" ")


stack = Stack()
stack.pushelement(34)
stack.pushelement(1)
stack.pushelement(98)
stack.pushelement(12)
stack.pushelement(100)
stack.displayStack()
print()

stack.popElement()
stack.displayStack()
print()

print("peekElementing element is: ",end=" ")
stack.peekElement()
