class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        res = s[0]
        last = s[0]
        count = 1
        for i in range(1,n):
            if s[i] != last:
                last = s[i]
                count = 0
            
            count += 1
            if count > 2:
                continue
            
            res += s[i]

        return res


        

        