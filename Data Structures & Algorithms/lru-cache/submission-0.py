class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.hashMap = {}
        self.cap = capacity
        self.aval = capacity
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.movRight(key)
            return self.hashMap[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.hashMap[key] = value
            self.movRight(key)
        else:
            if self.aval > 0:
                self.hashMap[key] = value
                self.tail.next = ListNode(key)
                self.tail = self.tail.next
                self.aval -= 1
            else:
                self.hashMap.pop(self.head.next.val, None)
                self.head.next = self.head.next.next
                if not self.head.next: self.tail = self.head
                self.aval += 1
                self.put(key, value)

    def movRight(self, val: int):
        cur = self.head
        while cur.next:
            if cur.next.val == val:
                node = cur.next
                cur.next = node.next
                if not cur.next: self.tail = cur
                self.tail.next = node
                self.tail = node
                self.tail.next = None
                break
            else:
                cur = cur.next
