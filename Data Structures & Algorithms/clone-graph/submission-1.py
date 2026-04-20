"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        o_n = {}

        def dfs(nd):
            if nd not in o_n:
                c = Node(nd.val)
                o_n[nd] = c
            else:
                return o_n[nd]
            for n in nd.neighbors:
                c.neighbors.append(dfs(n))
            return c
        return dfs(node)

        