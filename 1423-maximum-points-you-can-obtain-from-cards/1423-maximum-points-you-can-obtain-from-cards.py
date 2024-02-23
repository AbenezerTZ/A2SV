class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window = len(cardPoints) - k  
        total = sum(cardPoints)
        if k == len(cardPoints):
            return total
        mini = sum(cardPoints[:window])
        temp = mini
        for i in range(1, len(cardPoints) - window + 1): 
            temp -= cardPoints[i-1]
            temp += cardPoints[i + window - 1]
            mini = min(mini , temp)
        return total - mini
        