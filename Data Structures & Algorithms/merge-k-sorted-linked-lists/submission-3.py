# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from bisect import bisect_left

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return_lst = []
        while lists:
            curr = lists.pop()
            while curr:
                val = curr.val
                return_lst.insert(bisect_left(return_lst, val), val)
                curr = curr.next
        node = ListNode()
        start = node
        if return_lst:
            node.val = return_lst[0]
            if len(return_lst) > 1:
                for elem in return_lst[1:]:
                    next_node = ListNode()
                    node.next = next_node
                    node = next_node
                    node.val = elem
            return start
        return None
