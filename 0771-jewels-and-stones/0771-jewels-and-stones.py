class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewels = list(jewels)
        freq = Counter(jewels)
        count = 0
        for i in range (len(stones)):
            if stones[i] in freq:
                count += 1
        return count
        