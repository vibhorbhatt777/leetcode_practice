class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n= len(nums)
        total_subsets = 1 << n
        result  = []
        for num in range(0,total_subsets):
            lst = []
            for i in range(0,n):
                if num & (1<<i) != 0:
                    lst.append(nums[i])
        
            result.append(lst)

        return result


        