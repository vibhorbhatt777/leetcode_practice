class Solution:
    def climbStairs(self, n: int,mem = {}) -> int:
        if n <= 2:
           return n
        if n in mem:
           return mem[n]
        mem[n] = self.climbStairs(n-1, mem) + self.climbStairs(n-2, mem)
        return mem[n]

        