class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        s = set()
        res = []
        for i in range(n):
            for j in range(i+1,n):
                k = j + 1
                l = n - 1
                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target:
                        s.add((nums[i],nums[j],nums[k],nums[l]))
                        k+=1
                        l-=1
                    elif sum < target:
                        k+=1
                    else:
                        l-=1
        
        res = list(s)
        return res
        

        

        