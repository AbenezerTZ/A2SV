class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        empty=""
        def result(i):
            if len(str1) % i or len(str2) % i:
                return False
            fact1 = len(str1)//i
            fact2= len(str2)//i
            return str1[:i] * fact1 == str1 and str1[:i] * fact2 == str2
        for i in range(min(len(str1),len(str2)), 0,-1):
            if result(i):
                return str1[:i]
        return ""

        