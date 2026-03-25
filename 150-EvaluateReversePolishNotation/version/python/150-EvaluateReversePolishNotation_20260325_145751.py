# Last updated: 3/25/2026, 2:57:51 PM
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        stack=[]
4        for c in tokens:
5            if c == "+":
6                stack.append(stack.pop() + stack.pop())
7            elif c == "-":
8                b, a = stack.pop(), stack.pop()
9                stack.append(a - b)
10            elif c == "*":
11                stack.append(stack.pop() * stack.pop())
12            elif c == "/":
13                b, a = stack.pop(), stack.pop()
14                stack.append(int(float(a) / b))
15            else:
16                stack.append(int(c))
17        return stack[0]
18