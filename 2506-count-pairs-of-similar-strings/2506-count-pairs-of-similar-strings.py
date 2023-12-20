class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        uniqe = []
        for i in words:
            uniqe.append(set(i))
        print(uniqe)
        count = 0
        for i in range(len(words)-1):
            for k in range(i+1,len(words)):
                if(all(j in uniqe[k] for j in uniqe[i])) and len(uniqe[i])==len(uniqe[k]):
                    count+=1
        return count
        