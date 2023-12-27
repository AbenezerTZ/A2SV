class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        colors = list(colors)
        total = 0
        i = 0
        while i < len(colors)-1:
            temp = []
            flag = False
            while i < len(colors)-1 and colors[i]==colors[i+1]:
                flag = True
                temp.append(neededTime[i])
                i += 1
            if flag:
                temp.append(neededTime[i])
                total += sum(temp) - max(temp)
                i += 1
            else:
                i += 1
        return total 