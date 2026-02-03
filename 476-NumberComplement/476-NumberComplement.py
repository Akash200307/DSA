# Last updated: 2/3/2026, 9:39:10 PM
class Solution:
    def findComplement(self, num: int) -> int:
        length=num.bit_length()
        mask=(1<<length)-1
        return num^mask

        