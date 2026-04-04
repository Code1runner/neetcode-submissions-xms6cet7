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
        q = collections.deque()
        q.append(node)
        visited = set()
        visited.add(node)

        cloned = {}
        while q:
            n = q.popleft()
            if n not in cloned:
                cloned[n] = Node(n.val)
            copy = cloned[n]
            for neigh in n.neighbors:
                if neigh not in cloned:
                    cloned[neigh] = Node(neigh.val)
                cloned[n].neighbors.append(cloned[neigh])
                if neigh not in visited:
                    visited.add(neigh)
                    q.append(neigh)
        
        return cloned[node]
