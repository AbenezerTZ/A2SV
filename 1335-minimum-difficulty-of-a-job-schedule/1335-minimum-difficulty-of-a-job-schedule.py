class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        @cache
        def dp(idx, rmd):
            if not rmd or idx == n: 
                if not rmd and idx == n:
                    return 0
                return float('inf')

            maxi = -1
            mini = ans = float('inf')

            for i in range(idx, n - rmd + 1):
                maxi = max(maxi, jobDifficulty[i])
                mini = min(dp(i + 1, rmd - 1), mini)
                ans = min(ans, maxi + mini)
            
            return ans
        
        return dp(0, d)