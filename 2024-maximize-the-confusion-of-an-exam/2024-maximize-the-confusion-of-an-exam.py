class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i = j = 0
        maxi = 1
        t = f = 0
        while j < len(answerKey):
            if answerKey[j] == "T":
                t += 1
            else:
                f += 1
            mini = min(t,f)
            while mini > k:
                maxi = max(maxi,j - i)
                if answerKey[i] == "T":
                    t -= 1
                else:
                    f -= 1
                i += 1
                mini = min(t,f)
            j += 1
        maxi = max(maxi,j - i)
        return maxi
            