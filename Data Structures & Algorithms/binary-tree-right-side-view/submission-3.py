# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    def rightSideView(self, root: Optional['TreeNode']) -> List[int]:
        result = []
        if not root:
            return result

        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                
                # If this is the last node in the current level, add it to result
                if i == level_size - 1:
                    result.append(node.val)
                
                # Add left and right children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result