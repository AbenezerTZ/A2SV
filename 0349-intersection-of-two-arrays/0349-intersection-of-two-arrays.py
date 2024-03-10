class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = Counter(nums1)
        ans = []
        nums2 = set(nums2)
        for i in nums2:
            if i in freq:
                ans.append(i)
        return ans
        