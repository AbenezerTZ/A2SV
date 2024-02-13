class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for i in range(len(words)):
            temp = words[i][::-1]
            if words[i] == temp:
                return words[i]
        return ""