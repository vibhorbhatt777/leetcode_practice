class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        phone_map = {
            '2':'abc' ,'3':'def' , '4':'ghi','5':'jkl',
            '6':'mno' ,'7':'pqrs','8':'tuv','9':'wxyz'
        }
        memo = {}
        def solve(remaining_digits):
            #no more digit to process
            if not remaining_digits:
                return[""] 
            
            if remaining_digits in memo:
                return memo[remianing_digits]
            
            #compute and store
            first_digit = remaining_digits[0]
            rest_digits = remaining_digits[1:]

            #get all combination for the rest of the digits
            rest_combinations = solve(rest_digits)

            #combine current digits letter with rest combination
            current_combinations = []
            for letter in phone_map[first_digit]:
                for combo in rest_combinations:
                    current_combinations.append(letter + combo)

            #store in memo and return 
            memo[remaining_digits] = current_combinations
            return current_combinations
        
        return solve(digits)
        