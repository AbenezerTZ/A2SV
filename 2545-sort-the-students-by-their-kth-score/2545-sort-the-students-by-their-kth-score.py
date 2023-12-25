class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        mat = {}
        keys = []
        res = []
        for i in range(len(score)):
            mat[score[i][k]] = tuple(score[i])
            keys.append(score[i][k])
        keys.sort(reverse=True)
        for i in keys:
            res.append(mat[i])
        return res