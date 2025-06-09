class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res= []
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                j=i+1
                k=n-1
                while(j<k):
                    sums = nums[i]+nums[j]+nums[k]
                    if sums>0:
                        k-=1
                    elif sums<0:
                        j+=1
                    else:
                        res.append([nums[i],nums[j],nums[k]])
                        j+=1
                        k-=1
                        while(j<k and nums[j]==nums[j-1]):
                            j+=1
                        while(j<k and nums[k]==nums[k+1]):
                            k-=1

        return res

        
        