# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 -> 1 -> 2 -> 3
        # 3 -> 2 -> 1 -> 0

        # prev, cur = 0, head
        # 0 -> 1
        # tmp = prev
        # cur = tmp
        # prv = tmp
        # cur.next =
        # head.next
        # cur
        # tmp = head

        prev, curr = None, head

        while curr:
            temp = curr.next # 2
            curr.next = prev # 0
            prev = curr
            curr = temp

        return prev