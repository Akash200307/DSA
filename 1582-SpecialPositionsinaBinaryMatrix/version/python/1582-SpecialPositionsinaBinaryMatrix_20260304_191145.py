# Last updated: 3/4/2026, 7:11:45 PM
1class Solution:
2    def numSpecial(self, mat: List[List[int]]) -> int:
3        row_one_count = []
4        col_one_count = []
5
6        for i in range(len(mat)):
7            one_count = 0
8            for j in range(len(mat[0])):
9                if(mat[i][j] == 1):
10                    one_count += 1
11
12            row_one_count.append(one_count)
13
14        for j in range(len(mat[0])):
15            one_count = 0
16            for i in range(len(mat)):
17                if(mat[i][j] == 1):
18                    one_count += 1
19            col_one_count.append(one_count)
20        
21        count = 0
22        for i in range(len(mat)):
23            for j in range(len(mat[0])):
24
25                if(mat[i][j] == 1):
26
27                    if(row_one_count[i] == 1 and col_one_count[j] == 1):
28                        count += 1
29                        
30        return count