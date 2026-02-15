# Last updated: 2/15/2026, 10:31:20 PM
1class TrieNode:
2    def __init__ (self):
3        self.d={}
4        self.end=False
5
6class Trie:
7
8    def __init__(self):
9        self.root=TrieNode()
10
11    def insert(self, word: str) -> None:
12        cur=self.root
13
14        for i in word:
15            if i not in cur.d:
16                cur.d[i]=TrieNode()
17            cur=cur.d[i]
18        
19        cur.end=True
20
21    def search(self, word: str) -> bool:
22        cur =self.root
23
24        for i in word:
25            if i not in cur.d:
26                return False
27            cur=cur.d[i]
28        
29        return cur.end
30
31    def startsWith(self, prefix: str) -> bool:
32        
33        cur=self.root
34        for i in prefix:
35            if i not in cur.d:
36                return False
37            cur=cur.d[i]
38        return True
39        
40
41
42# Your Trie object will be instantiated and called as such:
43# obj = Trie()
44# obj.insert(word)
45# param_2 = obj.search(word)
46# param_3 = obj.startsWith(prefix)