# Last updated: 2/13/2026, 9:33:32 PM
1class Tries:
2    def __init__ (self):
3        self.d={}
4        self.end=False
5
6class Trie:
7
8    def __init__(self):
9        self.root=Tries()
10
11    def insert(self, word: str) -> None:
12        curr=self.root
13
14        for c in word:
15            if c not in curr.d:
16                curr.d[c]=Tries()
17            curr=curr.d[c]
18        curr.end=True
19
20
21    def search(self, word: str) -> bool:
22        curr=self.root
23        for c in word:
24            if c not in curr.d:
25                return False
26            curr=curr.d[c]
27
28        return curr.end
29
30    def startsWith(self, prefix: str) -> bool:
31        
32        curr=self.root
33
34        for c in prefix:
35            if c not in curr.d:
36                return False
37            curr=curr.d[c]
38        return True
39
40
41# Your Trie object will be instantiated and called as such:
42# obj = Trie()
43# obj.insert(word)
44# param_2 = obj.search(word)
45# param_3 = obj.startsWith(prefix)