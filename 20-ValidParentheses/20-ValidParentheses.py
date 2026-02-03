# Last updated: 2/3/2026, 9:44:00 PM
class Solution:
    def isValid(self, s: str) -> bool:

        level=[]

        for ch in s:
            if ch in "({[":
                level.append(ch)
            else:
                if not level:
                    return False
                top=level.pop()

                if ch==")" and top=="(" or ch =="}" and top=="{" or ch=="]" and top=="[":
                    continue
                else:
                    return False
        return not level
            
        