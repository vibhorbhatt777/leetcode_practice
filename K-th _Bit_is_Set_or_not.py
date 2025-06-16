class Solution:
    
    ''' n : int
        k : int
        Return Type : Boolean '''
    def checkKthBit(self, n, k):
        # Your code here
        # we want to check if the kth bit is set or not
        if n & (1<<k) != 0 :
            return True
        else:
            return False
        
