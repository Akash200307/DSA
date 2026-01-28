class Solution:
    def fib(self, n: int) -> int:
        self.dp=[-1]*(n+1)
        return self.helper(n)
    def helper(self,n):
        if n==1:
            return 1
        if n==0:
            return 0
        if self.dp[n]!=-1:
            return self.dp[n]
        self.dp[n]= self.helper(n-1)+self.helper(n-2)

        return self.dp[n]

        