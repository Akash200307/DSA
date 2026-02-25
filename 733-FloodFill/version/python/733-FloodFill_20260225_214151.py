# Last updated: 2/25/2026, 9:41:51 PM
1class Solution:
2    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
3        
4        dir=[(0,1),(1,0),(-1,0),(0,-1)]
5        rows=len(image)
6        cols=len(image[0])
7        initial_c=image[sr][sc]
8        q=deque()
9        if image[sr][sc]!=color:
10            q.append((sr,sc))
11            image[sr][sc]=color
12        while q:
13            for i in range(len(q)):
14                r,c=q.popleft()
15                for dr,dc in dir:
16                    row,col=dr+r,dc+c
17                    if row in range(rows) and col in range(cols) and image[row][col]==initial_c:
18                        q.append((row,col))
19                        image[row][col]=color
20        return image
21
22
23
24
25
26        
27