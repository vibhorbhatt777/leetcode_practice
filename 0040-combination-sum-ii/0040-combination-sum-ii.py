class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        def solve(index,curr_combination,rem_target):
            if rem_target == 0:
                result.append(list(curr_combination))
                return
            
            if rem_target < 0 :
                return
            
            for i in range(index,len(candidates)):
                candidate = candidates[i]

                if i > index and candidates[i] == candidates[i-1]:
                    continue

                curr_combination.append(candidate)

                solve(i+1,curr_combination , rem_target - candidate)
                curr_combination.pop()

        solve(0,[],target)
        return result


        