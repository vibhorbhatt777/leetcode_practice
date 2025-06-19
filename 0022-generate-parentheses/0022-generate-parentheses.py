class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        bracket = [""] * (n * 2)
        result = []
        
        def helper(index, balance, bracket, result):
            # Base case: if we've filled all positions
            if index >= len(bracket):
                if balance == 0:
                    result.append("".join(bracket))
                return
            
            # If balance is negative, we have more ')' than '(', invalid
            if balance < 0:
                return
            
            # If balance is greater than remaining positions, impossible to balance
            if balance > len(bracket) - index:
                return
            
            # Try placing '('
            bracket[index] = "("
            helper(index + 1, balance + 1, bracket, result)
            
            # Try placing ')'
            bracket[index] = ")"
            helper(index + 1, balance - 1, bracket, result)
        
        helper(0, 0, bracket, result)
        return result




            

        