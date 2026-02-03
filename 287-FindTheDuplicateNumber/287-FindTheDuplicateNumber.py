# Last updated: 2/3/2026, 9:39:31 PM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0
        fast=0

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break

        slow=0
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
            
        return slow
        
    
        