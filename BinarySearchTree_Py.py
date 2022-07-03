class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def makeTree(self, root, key):
        new_node = Node(key)
        new_node.left = None
        new_node.right = None
        return new_node

    def insertTree(self, root, key):
        if root == None:
            return self.makeTree(root, key)
        elif root.data > key:
            root.left = self.insertTree(root.left, key)
        else:
            root.right = self.insertTree(root.right, key)
        return root

    def successor(self, root):
        root = root.right
        while root.left != None:
            root = root.left
        return root

    def predessor(self, root):
        root = root.left
        while (root.right != None):
            root = root.right
        return root

    def deleteNode(self, root, value):
        if root is None:
            return root
        if root.data > value:
            root.left = self.deleteNode(root.left, value)
        elif root.data < value:
            root.right = self.deleteNode(root.right, value)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is not None:
                pre = self.predessor(root)
                root.data = pre.data
                root.left = self.deleteNode(root.left, root.data)
            else:
                pre = self.successor(root)
                root.data = pre.data
                root.right = self.deleteNode(root.right, root.data)
        return root

    def findNode(self, root, key):
        if root is None:
            return None
        if root.data == key:
            return root
        elif root.data > key:
            return self.findNode(root.left, key)
        else:
            return self.findNode(root.right, key)

    def displayBST(self, root):
        if root is None:
            return
        self.displayBST(root.left)
        print(root.data, end=" ")
        self.displayBST(root.right)


root = None
tree = BinarySearchTree()
root = tree.insertTree(root, 43)
root = tree.insertTree(root, 41)
root = tree.insertTree(root, 1)
root = tree.insertTree(root, 99)
root = tree.insertTree(root, 37)
tree.displayBST(root)
print()

print("After deleting 41")
root = tree.deleteNode(root, 41)
tree.displayBST(root)
print()

print("After findNode 37")
n = tree.findNode(root, 37)
if (n != None):
    print(f"{n.data} Found")
else:
    print("Not present in tree")
