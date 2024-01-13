class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        count = 0
        freq = {}
        for i in range(len(t)):
            if t[i] in freq:
                freq[t[i]] += 1
            else:
                freq[t[i]] = 1
        for j in range(len(s)):
            if s[j] in freq:
                if freq[s[j]] > 0 :
                    freq[s[j]] -= 1
                elif freq[s[j]] == 0:
                    count += 1
            else:
                count += 1
        return count
            
            