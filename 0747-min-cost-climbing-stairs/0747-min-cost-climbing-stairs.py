class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        memo = {}
        def solve(i):
            if i>=n:
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(solve(i+ 1), solve(i + 2))
            return memo[i]
        
        return min(solve(0),solve(1))


        