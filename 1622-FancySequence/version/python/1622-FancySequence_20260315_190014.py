# Last updated: 3/15/2026, 7:00:14 PM
1MOD = 10**9 + 7
2
3class Fancy:
4    def __init__(self):
5        self.raws = []      # raw[i]: independent of global state
6        self.mult = 1       # global accumulated multiplier
7        self.add  = 0       # global accumulated additive offset
8
9    def append(self, val: int) -> None:
10        # Store raw so that: raw * mult + add = val  (currently)
11        # raw = (val - add) * inv(mult)
12        raw = (val - self.add) * pow(self.mult, MOD - 2, MOD) % MOD
13        self.raws.append(raw)
14
15    def addAll(self, inc: int) -> None:
16        self.add = (self.add + inc) % MOD          # O(1)
17
18    def multAll(self, m: int) -> None:
19        self.mult = self.mult * m % MOD            # O(1)
20        self.add  = self.add  * m % MOD            # O(1) — crucial!
21
22    def getIndex(self, idx: int) -> int:
23        if idx >= len(self.raws):
24            return -1
25        return (self.raws[idx] * self.mult + self.add) % MOD