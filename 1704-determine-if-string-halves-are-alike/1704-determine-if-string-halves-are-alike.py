class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels =['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        right = 0
        for i in range(0,len(s)/2):
            if s[i] in vowels:
                left += 1
        for j in range(len(s)/2,len(s)):
            if s[j] in vowels:
                right += 1
        return left == right
        