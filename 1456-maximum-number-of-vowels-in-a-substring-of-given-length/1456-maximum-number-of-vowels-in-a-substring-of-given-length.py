class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set(["a", "e", "i", "o", "u"]) 
        s = list(s)
        max_vowels = 0
        current_window = 0
        for i in range(k):
            if s[i] in vowels:
                current_window += 1
        max_vowels = current_window
        for j in range(k, len(s)):
            if s[j] in vowels:
                current_window += 1
            if s[j - k] in vowels:
                current_window -= 1
            max_vowels = max(max_vowels, current_window)
        return max_vowels