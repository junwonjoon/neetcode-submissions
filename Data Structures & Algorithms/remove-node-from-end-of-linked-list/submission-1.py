# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = 0
        prev = None
        start = head
        length = 0
        while head:
            head = head.next
            length += 1
        head = start
        loop_counter = length - n
        #case when you have to remove first index
        if loop_counter <= 0:
            if head is None:
                return head
            else:
                return head.next
        else:
            while head and index < loop_counter:
                prev = head
                head = head.next
                index += 1
            if head:
                if prev is None:
                    return prev
                prev.next = head.next
            else:
                prev.next = None
            return start

