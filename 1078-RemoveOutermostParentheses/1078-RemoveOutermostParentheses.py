# Last updated: 2/3/2026, 9:37:52 PM
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        cn=0

        for c in s:
            if c=='(':
                if cn>0:
                    res+=c
                cn+=1
            elif c==')':
                cn-=1
                if cn>0:
                    res+=c
        return res

        
        