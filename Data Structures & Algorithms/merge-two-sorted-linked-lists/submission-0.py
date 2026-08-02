# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 and list2):
            if list1:
                return list1
            else:
                return list2
        curr1 = list1 
        curr2 = list2
        start = curr1 if curr1.val <= curr2.val else curr2 
        lst = [start]
        while curr1 or curr2:
            if not curr1:
                lst.append(curr2)
                curr2 = curr2.next
            elif not curr2:
                lst.append(curr1)
                curr1 = curr1.next
            elif curr1.val <= curr2.val:
                lst.append(curr1)
                curr1 = curr1.next
            else:
                lst.append(curr2)
                curr2 = curr2.next
        lst[-1].next = None
        for i in range(1, len(lst)):
            lst[i-1].next = lst[i]
        return start           
        