#User function Template for python3
class Solution:
    def longestSubarray(self, arr):
        #write code here
        """Brute frce apprach
        n = len(arr)
        maxi = 0
        for i in range(0,n):
            for j in range(i,n):
                if arr[j] < 0:
                    break
                
                curr_length = j-i+1
                maxi = max(maxi , curr_length)
        
        return maxi"""
        n = len(arr)
        maxi = curr_len = 0
        for i in range(0,n):
            curr_len = curr_len + 1 if arr[i]>=0 else 0
            maxi = max(maxi , curr_len)
            
        return maxi
                
                
    
    
    
