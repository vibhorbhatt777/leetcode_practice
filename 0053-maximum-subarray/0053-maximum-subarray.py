class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force way - give - TLE Error
        n = len(nums)
        maxi = float("-inf")
        """for i in  range(0,n):
            total = 0
            for j in range(i,n):
                total = total + nums[j]
                maxi = max(maxi , total)"""
                #kadans algorithm
        total = 0
        for i in range(0,n):
            total = total + nums[i]
            maxi = max(maxi,total)

            if total < 0:
                total = 0


            
        return maxi
        