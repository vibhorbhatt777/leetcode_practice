class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        def solve(index,curr_combination,rem_target,rem_count):
            if rem_count == 0 and rem_target == 0:
                return result.append(list(curr_combination))
                return

            if rem_count == 0 or rem_target <= 0 :
                return 

            for num in range(index,10):
                if num > rem_target:
                    break
                
            
                curr_combination.append(num)
                solve(num+1,curr_combination,rem_target-num,rem_count-1)
                curr_combination.pop()

        solve(1,[],n,k)
        return result
        