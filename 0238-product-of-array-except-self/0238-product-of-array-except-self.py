class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1]*n
        left_prod = [1]*n
        right_prod  = [1]*n

        left_prod[0] = 1
        for i in range(1,n):
            left_prod[i] = left_prod[i-1]*nums[i-1]
        
        right_prod[n-1] = 1
        for i in range(n-2,-1,-1):
            right_prod[i] = right_prod[i+1] * nums[i+1]
        
        for i in range(0,n):
            ans[i] = left_prod[i] * right_prod[i]
        
        return ans

        



        