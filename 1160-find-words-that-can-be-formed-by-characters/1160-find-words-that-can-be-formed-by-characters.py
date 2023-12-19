class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res = 0
        for i in range(len(words)):
            x=list(chars)
            count=0
            for j in range(len(words[i])):
                if words[i][j] in x:
                    x.remove(words[i][j])
                else:
                    count+=1
                    break
            if count==0:
                res+=len(words[i])
        return res