class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(firstList) == 0 or len(secondList)== 0:
            return []
        ans = []
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            temp = []
            if firstList[i][0] <= secondList[j][1]:
                if firstList[i][1] >= secondList[j][0]:
                    temp.append(max(firstList[i][0] ,secondList[j][0]))
                else:
                    i += 1
                    continue
            else:
                j += 1
                continue
            if firstList[i][1] < secondList[j][1]:
                temp.append(firstList[i][1])
                if i + 1 < len(firstList) and firstList[i+1][0] <= secondList[j][1]:
                    i += 1
                else:
                    i += 1
                    j += 1                    
            elif firstList[i][1] > secondList[j][1]:
                temp.append(secondList[j][1])
                if j + 1 < len(secondList) and secondList[j+1][0] <= firstList[i][1]:
                    j += 1
                else:
                    i += 1
                    j += 1   
            else:
                temp.append(secondList[j][1])
                i += 1
                j += 1
            ans.append(temp)
        return ans