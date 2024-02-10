class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        count = 0
        for n in range(1,len(s)):
            if s[:n+1] == s[n::-1]:
                count += 1
        i = 1
        while i < len(s)-1:   
            j = i + 1
            while j < len(s):
                if s[i:j+1] == s[j:i-1:-1]:
                    count += 1
                j += 1
            i += 1
        return count + len(s)