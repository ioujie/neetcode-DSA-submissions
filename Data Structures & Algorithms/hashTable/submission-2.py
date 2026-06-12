class Pair:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val

class LinkedList:
    def __init__(self, pair: Pair):
        self.pair = pair
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.mp = [None] * capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hashing(key)
        cur = self.mp[index]

        while cur:
            if cur.pair.key == key:
                cur.pair.val = value
                return
            cur = cur.next

        new_node = LinkedList(Pair(key, value))
        new_node.next = self.mp[index]
        self.mp[index] = new_node
        self.size += 1

        if self.size >= self.cap // 2:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hashing(key)
        cur = self.mp[index]
        while cur:
            if cur.pair.key == key:
                return cur.pair.val
            cur = cur.next
        return -1
        
    def remove(self, key: int) -> bool:
        index = self.hashing(key)
        cur = self.mp[index]
        prev = None
        while cur:
            if cur.pair.key == key:
                self.size -= 1
                if prev is None:
                    self.mp[index] = cur.next
                    return True
                prev.next = cur.next
                return True
            prev = cur
            cur = cur.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.cap

    def resize(self) -> None:
        old_mp = self.mp
        self.cap *= 2
        self.mp = [None] * self.cap

        for head in old_mp:
            cur = head
            while cur:
                next_node = cur.next
                index = self.hashing(cur.pair.key)
                cur.next = self.mp[index]
                self.mp[index] = cur
                cur = next_node

    def hashing(self, key: int) -> int:
        hashed = key % self.cap
        return hashed
