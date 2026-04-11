# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        prv = None
        k = self.getLen(head)
        i = 0
        while cur.next:
            prv = cur       
            cur = cur.next
            if i == k - n:
                prv.next = cur.next
                break
            i += 1

        return dummy.next

    def getLen(self, head):
        if not head:
            return 0
        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        return n