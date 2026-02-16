# Last updated: 2/16/2026, 1:13:44 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val = 0, neighbors = None):
5        self.val = val
6        self.neighbors = neighbors if neighbors is not None else []
7"""
8
9from typing import Optional
10class Solution:
11    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
12        
13        if not node:
14            return None
15        
16        oTn={}
17
18        def backtrack(node):
19
20            if node in oTn:
21                return oTn[node]
22            
23            oTn[node]=Node(val=node.val)
24
25            for nei in node.neighbors:
26                res=backtrack(nei)
27                oTn[node].neighbors.append(res)
28            
29            return oTn[node]
30
31        ans=backtrack(node)
32
33        return ans