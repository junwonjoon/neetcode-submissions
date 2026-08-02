# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import ceil
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lst_add = []
        lst_add.append(head)
        while head.next is not None:
            head = head.next
            lst_add.append(head)
        # 0 -> -1 -> 1 -> -2 
        prev_index = 0
        index = [-(ceil(i / 2)) if i % 2 == 1 else (ceil(i / 2)) for i in range(len(lst_add))]
        lst_add[index[-1]].next = None
        for i in range(1, len(index)):
            prev_i = index[i-1]
            curr_i = index[i]
            lst_add[prev_i].next = lst_add[curr_i]

            