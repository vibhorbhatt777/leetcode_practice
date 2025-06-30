class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        max_score = 0
        left = 0
        right = 0
        window_size = n - k
        min_window_sum = float('inf')
        if n == k:
            return sum(cardPoints)
        
        total_sum = sum(cardPoints)
        
        while right < n:
            max_score += cardPoints[right]
        
            while right - left + 1 > window_size:

                max_score -= cardPoints[left]
                left += 1
        
            if right - left + 1 == window_size:

                min_window_sum = min(min_window_sum, max_score)
            
            right += 1
        
        return total_sum - min_window_sum
        








