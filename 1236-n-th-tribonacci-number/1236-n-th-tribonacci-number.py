class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # this give tle error 
        # if n==0:
        #      return 0
        # if n==1 or n==2:
        #      return 1
        # return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1) 

        # lets do in o(n)
        A = [0] *(n+1)
        if(n==0 or n==1):
            return n
        if(n==2):
            return 1
        
        A[0] = 0
        A[1] = 1
        A[2] = 1
        for i in range(3,n+1):
            A[i] = A[i-1] + A[i-2] + A[i-3]
        
        return A[n]
        


        