class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Twin Walker approach - where input data is sorted
        n = len(numbers)
        left, right =0, n-1
        while left< right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                return [left+1,right+1]
            elif curr_sum < target:
                left+=1
            else:
                right-=1
            
        return []

        
