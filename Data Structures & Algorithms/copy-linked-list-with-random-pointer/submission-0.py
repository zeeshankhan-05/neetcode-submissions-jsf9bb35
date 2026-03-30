"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
    
        # 1. Create new nodes and insert them after the original nodes
        curr = head
        while curr:
            copiedNode = Node(curr.val)
            copiedNode.next = curr.next
            curr.next = copiedNode
            curr = copiedNode.next
        
        # 2. Set the random pointers for the new nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # 3. Separate the original and copied lists
        curr = head
        new_head = head.next
        while curr:
            copiedNode = curr.next
            curr.next = copiedNode.next
            if copiedNode.next:
                copiedNode.next = copiedNode.next.next
            curr = curr.next
        
        return new_head