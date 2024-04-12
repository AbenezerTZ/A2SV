class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        freq = {}
        maxi = i = 0
        temp = maxi
        for j in range(len(nums)):
            if nums[j] in freq and freq[nums[j]] == 0:
                freq[nums[j]] += 1
            elif nums[j] in freq and freq[nums[j]] == 1:
                temp -= nums[j]
                while nums[i] != nums[j]:
                    freq[nums[i]] -= 1
                    temp -= nums[i]
                    i += 1
                i += 1
            else:
                freq[nums[j]] = 1
            temp += nums[j]
            maxi = max(maxi,temp)
        return maxi
