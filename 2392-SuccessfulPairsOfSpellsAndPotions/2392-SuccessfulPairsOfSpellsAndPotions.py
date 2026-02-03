# Last updated: 2/3/2026, 9:36:35 PM
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
      potions.sort()
      ans=[]

      def bs(spell,potions,success):
        l,r=0,len(potions)-1
        idx=-1

        while l<=r:
          mid=(l+r)//2
          if(potions[mid]*spell>=success):
            idx=mid
            r=mid-1
          else:
            l=mid+1
        return idx

      for spell in spells:
        idx=bs(spell,potions,success)

        if(idx!=-1):
          ans.append(len(potions)-idx)
        else:
          ans.append(0)
      return ans
          


     

        


        
        
        