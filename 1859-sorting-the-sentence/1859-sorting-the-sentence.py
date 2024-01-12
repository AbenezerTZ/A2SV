class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        res = ""
        s = s.split()
        for i in range(len(s)):
            temp = []
            temp.append(s[i][-1])
            temp.append(s[i][:len(s[i])-1])
            ans.append(temp)
        ans.sort()
        for i in range(len(ans)):
            res += ans[i][1] + " "
        return res[:len(res)-1]