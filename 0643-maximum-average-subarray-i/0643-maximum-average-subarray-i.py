class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        w_sum = sum(nums[:k])
        m_sum = w_sum
        for j in range(k,len(nums)):
            w_sum += nums[j]-nums[i]
            m_sum = max(m_sum,w_sum)
            i += 1
        return (float(m_sum)/float(k))
        