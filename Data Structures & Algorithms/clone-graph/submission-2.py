"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned = defaultdict(list)

        def dfs(copy):
            if copy in cloned:
                return cloned[copy]
            
            new = Node(copy.val)
            cloned[copy] = new

            for i in copy.neighbors:
                new.neighbors.append(dfs(i))
            
            return new
        

        return dfs(node)