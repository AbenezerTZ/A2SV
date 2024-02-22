class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:  
        i = 0
        odd = sub = 0
        res = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 1:
                odd += 1
                sub = 0
            while odd == k:
                sub += 1
                if nums[i] % 2 == 1:
                    odd -= 1
                i += 1
            res += sub
        return res