class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        Len = lambda x: 1 if x < 2 else 2 if x < 10 else 3 if x < 100 else 4
        @cache
        def dp(i, k):
            if i < 0:
                return 0
            res = dp(i - 1, k - 1) if k else 9e9
            freq = 0
            
            for j in range(i, -1, -1):
                if s[i] == s[j]:
                    freq += 1
                elif k == 0:
                    return res
                else: k -= 1
                
                res = min(res, dp(j - 1, k) + Len(freq))
            
            return res
        
        return dp(len(s) - 1, k)