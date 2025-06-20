class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def solve(index,curr_combination,rem_target):
            if rem_target == 0:
                result.append(list(curr_combination))
                return
            
            if rem_target < 0 :
                return
            
            for i in range(index,len(candidates)):
                candidate = candidates[i]

                curr_combination.append(candidate)

                solve(i,curr_combination , rem_target - candidate)
                curr_combination.pop()

        solve(0,[],target)
        return result

        
        
        