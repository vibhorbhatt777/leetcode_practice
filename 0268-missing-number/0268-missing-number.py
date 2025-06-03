class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        for i in range(0,n):
            total+=nums[i]
        
        cal_sum = n*(n+1)/2

        miss_num = cal_sum - total

        return miss_num

        