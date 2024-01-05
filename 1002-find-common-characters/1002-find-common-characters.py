class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        ans = []
        for i in range(len(words)):
            temp = []
            for j in range(len(words[i])):
                temp.append(words[i][j])
            res.append(temp)
        for i in range(len(res[0])):
            flag = True
            for j in range(1,len(res)):
                if res[0][i] in res[j]:
                    res[j].remove(res[0][i])
                else:
                    flag = False
            if flag:
                ans.append(res[0][i])
        return ans