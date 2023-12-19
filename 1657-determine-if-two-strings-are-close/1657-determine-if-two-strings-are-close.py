class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        freq1={}
        freq2={}
        for i in word1:
            if i in freq1:
                freq1[i]+=1
            else:
                freq1[i]=1
        for j in word2:
            if j in freq2:
                freq2[j]+=1
            else:
                freq2[j]=1
        key1=sorted(list(freq1.keys()))
        key2=sorted(list(freq2.keys()))
        freq1=sorted(list(freq1.values()))
        freq2=sorted(list(freq2.values()))
        if freq1==freq2 and key1==key2:
            return True
        elif freq1==freq2 or key1!=key2:
            return False