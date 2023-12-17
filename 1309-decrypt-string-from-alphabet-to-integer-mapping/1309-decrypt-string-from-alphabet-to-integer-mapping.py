class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        alph = "0abcdefghijklmnopqrstuvwxyz"
        i=0
        res=""
        while i < len(s) :
            if i+2<len(s) and s[i+2]=="#":
                res += alph[int(s[i:i + 2])]
                i += 3
            else:
                res += alph[int(s[i])]
                i += 1
        return res
        

        