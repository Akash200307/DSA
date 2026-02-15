# Last updated: 2/15/2026, 10:51:32 PM
1class Trie:
2    def __init__ (self):
3        self.children={}
4        self.end=False
5
6class WordDictionary:
7
8    def __init__(self):
9        self.root=Trie()
10
11    def addWord(self, word: str) -> None:
12        curr=self.root
13
14        for c in word:
15            if c not in curr.children:
16                curr.children[c]=Trie()
17            curr=curr.children[c]
18        curr.end=True
19
20    def search(self, word: str) -> bool:
21
22        def dfs(j,root):
23            curr= root
24            for i in range(j,len(word)):
25                c=word[i]
26
27                if c=='.':
28                    for child in curr.children.values():
29                        if dfs(i+1,child):
30                            return True
31                    return False
32                
33                else:
34                    if c not in curr.children:
35                        return False
36                    curr=curr.children[c]
37            return curr.end
38
39        return dfs(0,self.root)
40
41
42# Your WordDictionary object will be instantiated and called as such:
43# obj = WordDictionary()
44# obj.addWord(word)
45# param_2 = obj.search(word)