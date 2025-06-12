#User function Template for python3

class Solution:
    def longestUniqueSubstring(self, s):
        # code here
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            #expand window
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            
            max_length = max(max_length , right-left + 1)
            
        return max_length
        
