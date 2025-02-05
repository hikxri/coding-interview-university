# Binary Search Tree

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        node = TreeNode(data)
        if data < self.data:
            if self.left is None:
                self.left = node
                return
            self.left.insert(data)
        else:
            if self.right is None:
                self.right = node
                return
            self.right.insert(data)

    def printInOrder(self):
        if self.data is None:
            return
        if self.left is not None:
            self.left.printInOrder()
        print(self.data, end=" ")
        if self.right is not None:
            self.right.printInOrder()

    def getNodeCount(self):
        if self.data is None:
            return 0
        l = r = 0
        if self.left is not None:
            l = self.left.getNodeCount()
        if self.right is not None:
            r = self.right.getNodeCount()
        return 1 + l + r


if __name__ == "__main__":
    myTree = TreeNode(5)

    myTree.insert(8)
    myTree.insert(32)
    myTree.insert(30)
    myTree.insert(10)
    myTree.insert(1)

    myTree.printInOrder()
    print()
    print(myTree.getNodeCount())
