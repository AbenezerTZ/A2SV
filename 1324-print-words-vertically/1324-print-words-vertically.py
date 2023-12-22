class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        s = s.split(" ")
        maxi = float('-inf')
        for i in range(len(s)):
            maxi = max(maxi, len(s[i]))
        for i in range(len(s)):
            while len(s[i]) != maxi:
                s[i] = s[i] + " "
        for i in range(maxi):
            temp = ""
            for j in range(len(s)):
                temp = temp + s[j][i]
            ans.append(temp)
        ans = [n.rstrip() for n in ans]
        return ans