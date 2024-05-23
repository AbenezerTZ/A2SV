class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prefsum = 0
        dic = {0:1}
        for num in nums:
            prefsum += num
            if  prefsum-k  in  dic:
                ans = ans + dic[prefsum-k]
            dic[prefsum] = dic.get(prefsum, 0) + 1
        return ans
       