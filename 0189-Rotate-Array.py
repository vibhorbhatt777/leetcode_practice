class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """  # l  (  o
        #brute force approch
        n = len(nums)
        k = k % n

        """for i in range(0,rotation):
            e = nums.pop()
            nums.insert(0,e)"""
            #slicing techq:-
        nums[:] = nums[n-k:] + nums[:n-k]
        

            
