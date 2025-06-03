class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        n = len(nums)
        nums2 = []
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target :
                    return [i,j]

        
        return []"""
        """n = len(nums)
        freq_map = {}
        for i , num in enumerate(n):
            complement = target - num
            if complement in freq_map:
                return [freq_map[complement],i]
            freq_map[num] = -1

        return []"""
        n = len(nums)
        for i in range(0,n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    return[i,j]
        
        return []
        
        
