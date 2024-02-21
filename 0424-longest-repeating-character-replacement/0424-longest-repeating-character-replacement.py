class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = {}
        res = 0
        i = 0
        for j in range(len(s)):
            if s[j] in freq:
                freq[s[j]] += 1
            else:
                freq[s[j]] = 1
            while ((j - i + 1) - max(freq.values())) > k:
                freq[s[i]] -= 1
                i += 1
            res = max(res , j - i + 1)
        return res
        