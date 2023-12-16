class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        sentence=set(sentence)
        if len(sentence)==26:
            return True
        else:
            return False
        