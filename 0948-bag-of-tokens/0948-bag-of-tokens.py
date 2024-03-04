class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        score = 0
        tokens.sort()
        maxi = 0
        i = 0
        j = len(tokens)-1
        
        if len(tokens) == 0:
            return 0
        elif len(tokens) == 1:
            if tokens[0] <= power:
                return 1
            else:
                return 0
            
        while i <= j:
            if tokens[i] <= power:
                score += 1
                power -= tokens[i]
                i += 1
            else:
                if score > 0:
                    power += tokens[j]
                    score -= 1
                    j -= 1
                else:
                    return maxi
                                        
            maxi = max(maxi, score)
        return maxi