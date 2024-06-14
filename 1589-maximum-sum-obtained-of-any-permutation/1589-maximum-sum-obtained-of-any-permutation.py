class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        maxi = 10**9 + 7
        ans = 0
        index = n - 1
        range_sum = [0] * n
        
        for req in requests:
            range_sum[req[0]] += 1

            if req[1] + 1 < n:
                range_sum[req[1] + 1] -= 1

        
        for i in range(1, n):
            range_sum[i] += range_sum[i - 1]
        nums.sort()
        range_sum.sort()

       
        while index >= 0 and range_sum[index] > 0:
            ans = (ans + nums[index] * range_sum[index]) % maxi
            index -= 1

        return ans
        