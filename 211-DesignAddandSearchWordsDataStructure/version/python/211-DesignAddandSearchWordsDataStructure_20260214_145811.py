# Last updated: 2/14/2026, 2:58:11 PM
1class Trie:
2    __slots__ = ['children', 'end']  # ✅ Memory optimization
3    
4    def __init__(self):
5        self.children = {}
6        self.end = False
7
8
9class WordDictionary:
10    def __init__(self):
11        self.root = Trie()
12
13    def addWord(self, word: str) -> None:
14        curr = self.root
15        for c in word:
16            if c not in curr.children:
17                curr.children[c] = Trie()
18            curr = curr.children[c]
19        curr.end = True
20
21    def search(self, word: str) -> bool:
22        def dfs(i, node):
23            # ✅ Base case check before loop
24            if i == len(word):
25                return node.end
26            
27            c = word[i]
28            
29            if c == '.':
30                # ✅ Early termination: return immediately on first match
31                return any(dfs(i + 1, child) for child in node.children.values())
32            else:
33                # ✅ Direct lookup and early return
34                if c not in node.children:
35                    return False
36                return dfs(i + 1, node.children[c])
37        
38        return dfs(0, self.root)
39