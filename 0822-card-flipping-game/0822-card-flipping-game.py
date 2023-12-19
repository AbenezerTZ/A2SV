class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        temp = []
        res = []
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                temp.append(fronts[i]) 
        for i in range(len(backs)):
            if backs[i] not in temp:
                res.append(backs[i])
        for i in range(len(backs)):
            if fronts[i] not in temp:
                res.append(fronts[i])
        if len(res)==0:
            return 0
        else:
            return min(res)