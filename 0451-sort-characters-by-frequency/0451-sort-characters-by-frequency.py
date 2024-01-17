class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        freq = {}
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1
        key = []
        for i,j in freq.items():
            temp = []
            temp.append(j)
            temp.append(i)
            key.append(temp)
        key.sort(reverse = True)
        for i in range(len(key)):
            ans += key[i][1] * key[i][0]
        return ans