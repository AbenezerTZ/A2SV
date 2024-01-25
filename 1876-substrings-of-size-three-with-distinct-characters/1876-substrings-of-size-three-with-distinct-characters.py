class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)-2):
            if len(set(s[i:i+3])) == len(s[i:i+3]):
                count += 1
        return count
                
            
        