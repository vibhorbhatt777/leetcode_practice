class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """using brute force approach"""
        pos = []
        neg = []
        a = len(nums)
        for i in range(0,a):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
            
        n = len(pos) 
        for i in range(0,n):
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]

        return nums
