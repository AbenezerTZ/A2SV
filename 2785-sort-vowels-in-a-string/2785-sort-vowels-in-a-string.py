class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = {"A":0,"E":1,"I":2,"O":3,"U":4,"a":5,"e":6,"i":7,"o":8,"u":9}
        order = []
        num = []
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowel:
                order.append(s[i])
                num.append(i)
        order.sort()
        num.sort()
        for j in range(len(order)):
            s[num[j]] = order[j]
        return "".join(s)
        
        