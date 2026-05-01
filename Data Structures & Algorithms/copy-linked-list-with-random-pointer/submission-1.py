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
        lst = defaultdict(lambda:Node(0))
        lst[None] = None

        cur = head
        while cur:
            lst[cur].val = cur.val
            lst[cur].next = lst[cur.next]
            lst[cur].random = lst[cur.random]
            cur = cur.next
        return lst[head]