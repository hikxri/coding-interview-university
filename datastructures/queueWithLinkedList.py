import doublyLinkedList as dl


class Queue:
    def __init__(self):
        self.data = dl.DoublyLinkedList()

    def isEmpty(self):
        return self.data.head is None

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.popFront()

    def traverse(self):
        self.data.traverse()


if __name__ == "__main__":
    myQueue = Queue()
    print(myQueue.isEmpty())
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.traverse()
    print(myQueue.dequeue())
    print(myQueue.dequeue())
    print(myQueue.dequeue())
