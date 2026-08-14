# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        set_visted = set()
        while head:
            set_visted.add(head)
            head = head.next
            if head in set_visted:
                return True
        return False