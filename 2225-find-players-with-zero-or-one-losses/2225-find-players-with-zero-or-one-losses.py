class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        wins = {}
        lose = {}
        res = []
        for a,b in matches:
            wins[a] = wins.get(a,0) + 1
            lose[b] = lose.get(b,0) + 1
        temp = []
        for i in wins:
            if i not in lose:
                temp.append(i)
        temp.sort()
        res.append(temp)
        temp = []
        for a,b in lose.items():
            if b==1:
                temp.append(a)
        temp.sort()
        res.append(temp)
        return res