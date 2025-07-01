class Solution:
    def fractionalknapsack(self, val, wt, capacity):
        #code here
        res = []
        n = len(val)
        for i in range(0,n):
            res.append((val[i],wt[i]))
        
        res.sort(key=lambda x: x[0]/x[1], reverse=True)
        
        curr_weight = 0
        final_value = 0.0
        for i in range(0,len(res)):
            if curr_weight + res[i][1] <= capacity:
                curr_weight += res[i][1]
                final_value += res[i][0]
            else:
                rem = capacity - curr_weight
                cost = res[i][0]/res[i][1] * rem
                final_value += cost
                break
            
        return final_value
