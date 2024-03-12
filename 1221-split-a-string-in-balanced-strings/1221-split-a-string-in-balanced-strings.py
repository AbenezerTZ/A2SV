class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = r = 0
        count = 0
        for i in s:
            if i == "L":
                l += 1
            else:
                r += 1
            if r == l:
                count += 1
                r = l = 0
        return count
        