class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        orders = {}
        for i in range(len(order)):
            orders[order[i]] = i
        for i in range (len(words)-1):
            mini = min(len(words[i]),len(words[i+1]))
            count = 0
            for j in range(mini):
                if orders[words[i][j]] > orders[words[i+1][j]]:
                    return False
                elif orders[words[i][j]] < orders[words[i+1][j]]:
                    break
                elif orders[words[i][j]] == orders[words[i+1][j]]:
                    count+=1
            if count==mini and len(words[i]) > len(words[i+1]) :
                return False
        return True
                
        