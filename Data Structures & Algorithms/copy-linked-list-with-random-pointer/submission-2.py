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

        curr = head
        index = 0
        new_nodes = defaultdict()
        new_start = None
        prev = None
        random = defaultdict()

        while curr:
            local_new_node = Node(curr.val, random= curr.random)

            if prev:
                prev.next = local_new_node

            else:
                new_start = local_new_node

            random |= {curr: local_new_node}
            prev = local_new_node
            index += 1
            curr = curr.next

        curr = new_start

        while curr:
            if curr.random:
                curr.random = random[curr.random]
            curr = curr.next

        return new_start

        