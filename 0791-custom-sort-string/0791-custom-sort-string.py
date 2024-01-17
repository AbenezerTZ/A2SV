class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        ans = ""
        freq = {}
        dic = {}
        for i in range(len(order)):
            dic[i] = order[i]
        for j in range(len(s)):
            if s[j] in freq:
                freq[s[j]] += 1
            else:
                freq[s[j]] = 1
        for i in range(len(dic)):
            if dic[i] in freq:
                ans += dic[i] * freq[dic[i]]
        for key,value in freq.items():
            if key not in dic.values():
                ans += key * value
        return ans
            
            