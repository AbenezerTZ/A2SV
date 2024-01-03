class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        res = []
        for i in bank:
            if i.count("1") >= 1:
                res.append(i.count("1")) 
        count = 0
        for i in range(len(res)-1):
            count += res[i] * res[i+1]
        return count
            