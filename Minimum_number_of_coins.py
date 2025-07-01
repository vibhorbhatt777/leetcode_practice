#User function Template for python3

class Solution:
    def minPartition(self, N):
        # code here
        coins = [1,2,5,10,20,50,100,200,500,2000]
        res = []
        n = len(coins)
        for i in range(n-1,-1,-1):
            while N >= coins[i]:
                res.append(coins[i])
                N -= coins[i]
        
        return res
