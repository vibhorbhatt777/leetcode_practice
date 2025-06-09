class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #lower bound and upper bound 
        n = len(nums)
        lb = n
        low , high = 0, n-1
        while low<=high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                lb = mid
                high =  mid - 1
            else:
                low = mid + 1
            
        return lb

        
            
            
            

        