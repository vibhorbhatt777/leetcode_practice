class Solution(object):
    def subsets(self, num):
        result = []
# now we can learn using recursion and backtracking
        def solve(index,subset):
            if index>= len(num):
                result.append(list(subset))
                return 
                
            subset.append(num[index])
            solve(index+1,subset)
            subset.pop()
            solve(index+1,subset)


        solve(0,[])

        return result 

                



        


        
