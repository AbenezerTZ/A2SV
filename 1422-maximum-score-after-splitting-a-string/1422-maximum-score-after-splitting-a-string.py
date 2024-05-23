class Solution:
    def maxScore(self, s: str) -> int:
        tot = one = zero =  0
        maxi = 0
        for i in s:
            if i == "1":
                tot += 1
        for i in range(0,len(s)-1):
            if s[i] == "1":
                one += 1
            else:
                zero += 1
            maxi = max(maxi,(tot - one + zero))
        return maxi