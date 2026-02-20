# Last updated: 2/20/2026, 7:28:37 PM
1
2class Solution:
3    def makeLargestSpecial(self, s: str) -> str:
4        if s == '':
5            return ''
6        ans = []
7        cnt = 0
8        i = j = 0
9        while i < len(s):
10            cnt += 1 if s[i] == '1' else -1
11            if cnt == 0:
12                ans.append('1' + self.makeLargestSpecial(s[j + 1 : i]) + '0')
13                j = i + 1
14            i += 1
15        ans.sort(reverse=True)
16        return ''.join(ans)