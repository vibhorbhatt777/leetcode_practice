class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n-2): 
            # fix first element (need atleast 3 element)
            if i > 0 and nums[i] == nums[i-1]:
                continue

            #now use twin walker approach - inward traversal
            left , right = i+1 , n-1
            target = -nums[i] # i want nums[left] + nums[right] = -nums[i]

            while left < right:
                curr_sum = nums[left] + nums[right]

                if curr_sum == target:
                    result.append([nums[i],nums[left],nums[right]])

                    #skip duplicates for left pointer
                    while left < right and nums[left] == nums[left+1]:
                        left +=1

                    #skip duplicates for right pointer
                    while left < right and nums[right] == nums[right-1]:
                        right-=1
                    
                    left+=1
                    right -=1
                
                elif curr_sum < target:
                    left+=1
                else:
                    right-=1
        
        return result




        

        
        