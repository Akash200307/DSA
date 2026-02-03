# Last updated: 2/3/2026, 9:42:19 PM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        for i in range(1,numRows+1):
            res.append(self.generateRow(i))
        return res

    

    def generateRow(self,r):
        ans=1
        res=[]
        res.append(ans)

        for i in range(1,r):
            ans=ans*(r-i)
            ans=ans//i
            res.append(ans)
        return res