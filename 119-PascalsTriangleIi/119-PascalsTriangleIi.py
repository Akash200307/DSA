# Last updated: 2/3/2026, 9:42:17 PM
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=1
        res=[]
        res.append(1)
        rowIndex=rowIndex+1
        for i in range(1,rowIndex):
            ans=ans*(rowIndex-i)
            ans=ans//i
            res.append(ans)
        return res
    