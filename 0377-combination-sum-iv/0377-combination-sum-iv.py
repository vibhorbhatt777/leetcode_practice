class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # it cant be solve by using backtrack approach 
        memo = {}
        def dp(remaining):
            if remaining == 0: return 1
            if remaining < 0: return 0
            if remaining in memo : return memo[remaining]

            count = sum(dp(remaining-num) for num in nums)
            memo[remaining] = count
            return count
        
        return dp(target)


        