class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(0,n):
            nums[i] *=nums[i]
        nums.sort()
        return nums