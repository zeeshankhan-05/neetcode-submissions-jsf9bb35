# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Use fast and slow pointers to find the midpoint
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Seperate the first half and second half
        secondHalf = slow.next
        slow.next = None

        # 3. Reverse the second half
        prev = None
        while secondHalf:
            temp = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = temp
        secondHalf = prev

        # 4. Combine the reversed second half with the first half
        firstHalf = head
        while secondHalf:
            tempFirst = firstHalf.next
            tempSecond = secondHalf.next

            firstHalf.next = secondHalf
            secondHalf.next = tempFirst

            firstHalf = tempFirst
            secondHalf = tempSecond
