class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        s  = str(num)

        max_s = s
        for ch in s:
            if ch!='9':
                max_s = s.replace(ch,'9')
                break
        
        min_ch = s
        for ch in s:
            if ch !=0:
                min_ch = s.replace(ch,'0')
                break
        
        return int(max_s) - int(min_ch)

        


        
    


        