class Solution(object):
    def numDistinct(self, s, t):
        #create cache first
        memo = {}
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        def solve(s_index,t_index):

            #create cache first
            if(s_index , t_index) in memo:
                return memo[(s_index,t_index)]
            
            if t_index == len(t):
                return 1
            if s_index == len(s):
                return 0

            count = 0

                        
            #character match we have 2 choice to take it or skip it
            if s[s_index] == t[t_index]:
                count += solve(s_index+1,t_index+1)

            count+= solve(s_index+1,t_index) #skip the character from s
            #store result in memo
            memo[(s_index,t_index)] = count
            return count
        
        return solve(0,0)



        