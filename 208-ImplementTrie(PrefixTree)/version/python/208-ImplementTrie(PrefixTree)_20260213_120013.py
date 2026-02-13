# Last updated: 2/13/2026, 12:00:13 PM
1class Trie:
2
3    def __init__(self):
4        self.trie={}
5
6    def insert(self, word: str) -> None:
7        d=self.trie
8
9        for c in word:
10            if c not in d:
11                d[c]={}
12            d=d[c]
13        d["."]="."
14
15    def search(self, word: str) -> bool:
16
17        d=self.trie
18
19        for c in word:
20            if c not in d:
21                return False
22            d=d[c]
23        return "." in d
24        
25
26    def startsWith(self, prefix: str) -> bool:
27        
28        d=self.trie
29
30        for c in prefix:
31            if c not in d:
32                return False
33            d=d[c]
34        return True
35
36
37# Your Trie object will be instantiated and called as such:
38# obj = Trie()
39# obj.insert(word)
40# param_2 = obj.search(word)
41# param_3 = obj.startsWith(prefix)