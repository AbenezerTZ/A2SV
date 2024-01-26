class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        window = 1
        maxi = 1
        i = 0
        while i < len(s):
            while window < len(s) and len(list(s[i:window])) == len(set(list(s[i:window]))):
                window += 1
            if len(list(s[i:window])) == len(set(list(s[i:window]))):
                maxi = max(maxi,window-i)
            else:
                maxi = max(maxi,window-i-1)
            i += 1
            window = i + 1
        return maxi