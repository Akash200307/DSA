# Last updated: 4/9/2026, 8:32:03 PM
1class Solution:
2    MOD = 1000000007
3
4    def modExp(self, base, exp):
5        if exp == 0:
6            return 1
7        
8        half = self.modExp(base, exp // 2)
9        result = (half * half) % self.MOD
10
11        if exp % 2:
12            result = (result * base) % self.MOD
13
14        return result
15
16    def xorAfterQueries(self, arr, ops):
17        n = len(arr)
18        block = int(n ** 0.5) + 1
19
20        buckets = [[] for _ in range(block)]
21
22        for query in ops:
23            left, right, step, val = query
24
25            if step < block:
26                buckets[step].append(query)
27            else:
28                pos = left
29                while pos <= right:
30                    arr[pos] = (arr[pos] * val) % self.MOD
31                    pos += step
32
33        for step in range(1, block):
34            if not buckets[step]:
35                continue
36
37            multiplier = [1] * (n + step + 5)
38
39            for query in buckets[step]:
40                left, right, _, val = query
41
42                lastIndex = left + ((right - left) // step) * step
43                stop = lastIndex + step
44
45                multiplier[left] = (multiplier[left] * val) % self.MOD
46
47                invVal = self.modExp(val, self.MOD - 2)
48                multiplier[stop] = (multiplier[stop] * invVal) % self.MOD
49
50            for i in range(n):
51                if i - step >= 0:
52                    multiplier[i] = (multiplier[i] * multiplier[i - step]) % self.MOD
53
54            for i in range(n):
55                arr[i] = (arr[i] * multiplier[i]) % self.MOD
56
57        ans = 0
58        for value in arr:
59            ans ^= value
60
61        return ans