class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        word = list(word)
        i = 0
        if ch in word:
            j = word.index(ch)
        else:
            return "".join(word)
        while i < j:
            word[i],word[j] = word[j],word[i]
            i += 1
            j -= 1
        return "".join(word)
        