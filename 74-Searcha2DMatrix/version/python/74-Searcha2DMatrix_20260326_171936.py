# Last updated: 3/26/2026, 5:19:36 PM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        ROWS=len(matrix)
4        COLS=len(matrix[0])
5
6        top=0
7        bot=ROWS-1
8
9        while (top<=bot):
10            mid=(top+bot)//2
11            if target>matrix[mid][-1]:
12                top=mid+1
13            elif target<matrix[mid][0]:
14                bot=mid-1
15            else:
16                break
17        if not top<=bot:
18            return False
19        
20        l=0
21        r=COLS-1
22        row=(top+bot)//2
23        while(l<=r):
24            mid=(l+r)//2
25            if matrix[row][mid]==target:
26                return True
27            elif matrix[row][mid]<target:
28                l=mid+1
29            else:
30                r=mid-1
31        return False
32
33