# Last updated: 2/3/2026, 9:40:28 PM
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_st = {}
        map_ts = {}
        
        for c_s,c_t in zip(s,t):
            if c_s in map_st:
                if map_st[c_s]!=c_t:
                    return False
            else:
                map_st[c_s]=c_t
            
            if c_t in map_ts:
                if map_ts[c_t]!=c_s:
                    return False
            else:
                map_ts[c_t]=c_s
        return True

                    