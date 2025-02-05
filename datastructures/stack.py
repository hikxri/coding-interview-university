class Stack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        if self.peek() is None:
            return True
        return False

    def push(self, value):
        self.data.append(value)

    def pop(self):
        self.data.pop()

    def peek(self):
        return self.data[-1]

    def printAsArray(self):
        print(self.data)


if __name__ == "__main__":
    myStack = Stack()
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    myStack.printAsArray()
    myStack.pop()
    myStack.printAsArray()
    print("Peek:", myStack.peek())
