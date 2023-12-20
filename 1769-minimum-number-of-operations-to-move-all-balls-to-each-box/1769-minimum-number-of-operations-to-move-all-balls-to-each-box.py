class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        temp = []
        res = []       
        for i in boxes:
            temp.append(int(i))
        ones = []
        for i in range(len(temp)):
            if temp[i] == 1:
                ones.append(i)
                
        for i in range(len(temp)):
            total = 0
            for j in ones:
                total += abs(j-i)
            res.append(total)
        return res