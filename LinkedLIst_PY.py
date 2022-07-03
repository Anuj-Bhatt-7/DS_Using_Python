class Node:
    def __init__(self, data):
        self.data = data
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None

    def insertNode(self, new_data):
        new_node = Node(new_data)
        new_node.nextval = self.headval
        self.headval = new_node

    def deleteNode(self,key):
        temp = self.headval
        if(temp is not None):
            if(temp.data == key):
                self.headval = temp.nextval
                temp = None
                return
        while(temp is not None):

            if(temp.data == key):
                break
            prev = temp
            temp = temp.nextval
        if(temp == None):
            return
        prev.nextval = temp.nextval
        temp = None

    def displayList(self):
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

print("created Linked list")

list.displayList()
list.deleteNode(3)

print("After deleting element 3")
list.displayList()
