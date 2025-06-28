class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sort_nums = sorted(nums, reverse=True)
        k_large = sort_nums[:k]

        result = []
        count = {}
        for num in k_large:
            count[num] = count.get(num, 0) + 1 

        for num in nums:
            if num in count and count[num] > 0:
                result.append(num)
                count[num] -= 1
                if len(result) == k:
                    break
        
        return result


        