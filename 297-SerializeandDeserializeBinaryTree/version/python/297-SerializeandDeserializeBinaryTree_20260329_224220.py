# Last updated: 3/29/2026, 10:42:20 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Codec:
9
10    def serialize(self, root):
11        """Encodes a tree to a single string.
12        
13        :type root: TreeNode
14        :rtype: str
15        """
16        res=[]
17        def dfs(node):
18            if not node:
19                res.append("A")
20                return
21            res.append(str(node.val))
22            dfs(node.left)
23            dfs(node.right)
24        dfs(root)
25        return ",".join(res)
26
27    def deserialize(self, data):
28        """Decodes your encoded data to tree.
29        
30        :type data: str
31        :rtype: TreeNode
32        """
33        data=data.split(",")
34        self.i=0
35        def dfs():
36            val=data[self.i]
37            self.i+=1
38            if val=="A":
39                return None
40            node=TreeNode(int(val))
41            node.left=dfs()
42            node.right=dfs()
43            return node
44        return dfs()
45
46# Your Codec object will be instantiated and called as such:
47# ser = Codec()
48# deser = Codec()
49# ans = deser.deserialize(ser.serialize(root))