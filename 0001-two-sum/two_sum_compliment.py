class Solution(object):
    def twoSum(self, nums, target):
        
        n = len(nums)
        freq_map = {}
        for i in range(0,n):
            rem = target - nums[i]
            if rem in freq_map:
                return [freq_map[rem],i]
            
            freq_map[nums[i]] = i
        
        return []

        
        
