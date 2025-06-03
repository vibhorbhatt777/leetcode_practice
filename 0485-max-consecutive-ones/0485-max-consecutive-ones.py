class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        max_count = 0
        for i in range(0,n):
            if nums[i]==1:
                total+=1
            else:
                max_count = max(max_count, total)
                total = 0


        return max(max_count, total)

        