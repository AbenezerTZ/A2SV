class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        freq = Counter("".join(words))
        for key,value in freq.items():
            if value % len(words) != 0:
                return False
        return True
        