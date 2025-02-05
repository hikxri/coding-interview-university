import singlyLinkedList as sl


class HashTable:
    def __init__(self, size):
        self.size = size  # m
        self.data = [sl.SinglyLinkedList() for _ in range(size)]

    def hash(self, key):  # O(1)
        return key % self.size

    def insert(self, key, value):  # O(n) at worst case
        index = self.hash(key)
        self.data[index].append([key, value])

    def delete(self, key):
        dict_index = self.hash(key)
        list_index = self.data[dict_index].searchKey(key)
        if list_index != -1:
            self.data[dict_index].remove(list_index)

    def get(self, key):  # O(2n)
        index = self.hash(key)
        return self.data[index].access(self.data[index].searchKey(key))[1]
        # can be O(n) with a better get function

    def exists(self, key):  # O(n)
        index = self.hash(key)
        return self.data[index].searchKey(key) != -1

    def traverse(self):  # O(m * n)
        for linked_list in self.data:
            linked_list.traverse()


if __name__ == "__main__":
    myDict = HashTable(7)
    myDict.insert(5, "Hello")
    myDict.insert(1, "World")
    myDict.insert(2, "Hi")
    print(myDict.get(5))
    print(myDict.exists(5))
    myDict.delete(1)
    myDict.traverse()
