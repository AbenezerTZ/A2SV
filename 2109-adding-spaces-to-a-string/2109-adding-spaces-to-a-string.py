class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        start = 0
        res = []
        for i in spaces:
            res.append(s[start:i] + ' ') 
            start = i
        res.append(s[spaces[-1]:])
        res = ''.join(res)
        return (res[:len(s)+len(spaces)])