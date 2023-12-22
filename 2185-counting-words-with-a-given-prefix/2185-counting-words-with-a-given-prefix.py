class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        for i in words:
            if i[:len(pref)]==pref:
                count+=1
        return count
        