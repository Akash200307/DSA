# Last updated: 2/3/2026, 9:37:08 PM
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
            totalChalk=sum(chalk)
            remainingChalk=k%totalChalk
            for i in range(len(chalk)):
                if chalk[i]>remainingChalk:
                    return i
                remainingChalk-=chalk[i]
            return 0
        