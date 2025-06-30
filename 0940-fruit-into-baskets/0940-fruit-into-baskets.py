class Solution(object):
    def totalFruit(self, nums):
        """
        :type fruits: List[int]
        :rtype: int
        """
        max_length = 0
        n = len(nums)
        my_dict = {}
        left =0
        right = 0
        while right < n:
            my_dict[nums[right]] = my_dict.get(nums[right],0)+1
            if len(my_dict)>2:
                my_dict[nums[left]]-=1

                if my_dict[nums[left]] == 0:
                     del my_dict[nums[left]]
            
                left+=1

            if len(my_dict)<=2:
                max_length = max(max_length,right-left+1)
            
            right+=1
        
        return max_length
        