# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Find the length of the list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # 2. Find the nth node (length - n)
        curr = head
        prev = None
        for i in range(length - n):
            prev = curr
            curr = curr.next

        # 3. Remove the nth from the end
        if prev is None:
            head = head.next
        else:
            prev.next = curr.next

        return head