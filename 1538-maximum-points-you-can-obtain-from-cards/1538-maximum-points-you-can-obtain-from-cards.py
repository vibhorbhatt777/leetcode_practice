class Solution(object):
    def maxScore(self, nums, k):
        n = len(nums)
        if n == k:
            return sum(nums)
                 
        # Start with all k cards from left
        left_sum = sum(nums[:k])
        right_sum = 0
        maxi = left_sum
        
        # Try combinations: remove from left, add from right
        right_index = n - 1
        for i in range(k-1, -1, -1):  # Remove from position k-1 down to 0
            left_sum -= nums[i]      # Remove card from left
            right_sum += nums[right_index]  # Add card from right
            maxi = max(maxi, left_sum + right_sum)
            right_index -= 1
                  
        return maxi