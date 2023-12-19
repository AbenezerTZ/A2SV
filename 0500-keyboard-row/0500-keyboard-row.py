class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        check = ["QWERTYUIOPqwertyuiop","ASDFGHJJKLasdfghjkl","ZXCVBNMzxcvbnm"]
        for i in words:
            if all(char in check[0] for char in i):
                res.append(i)
            elif all(char in check[1] for char in i):
                res.append(i)
            elif all(char in check[2] for char in i):
                res.append(i)
        return res



        