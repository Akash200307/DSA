# Last updated: 2/3/2026, 9:41:45 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew={}

        def cloning(node):
            if node in oldToNew:
                return oldToNew[node]
            copy=Node(node.val)
            oldToNew[node]=copy
            for nei in node.neighbors:
                copy.neighbors.append(cloning(nei))
            return copy
            
        
        return cloning(node) if node else None