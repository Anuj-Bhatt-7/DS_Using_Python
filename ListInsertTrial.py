class Node:
    def __init__(self, data):
        self.data = data
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None

    def insertNode(self, new_data):
        new_node = Node(new_data)
        if self.headval is None:
            self.headval = new_node
            return
        last = self.headval
        while (last.nextval):
            last = last.nextval
        last.nextval = new_node


    def displayNode(self):
        printval = self.headval
        while(printval):
            print(f"{printval.data}  ")
            printval = printval.nextval


list = LinkedList()
list.insertNode(7)
list.insertNode(3)
list.insertNode(6)
list.insertNode(9)
list.insertNode(10)

data = int(input("Enter the data to insert"))
list.insertNode(data)

list.displayNode()
