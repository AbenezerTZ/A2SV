class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        if len(cards) == len(set(cards)):
            return -1
        window ={}
        mini = float('inf')
        for i in range(len(cards)):
            if cards[i] not in window:
                window[cards[i]] = i
            else:
                mini = min( mini, (i - window[cards[i]]) + 1)
                window[cards[i]] = i
        return mini
        