class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, len(s)-1
        count = 0
        while l < r:
            if s[l] == s[r]:
                c = s[l]
                while l < r and s[l] == c:
                    l += 1
                    count += 1
                if l == r:
                    l -= 1
                while r > l and s[r] == c:
                    r -= 1
                    count += 1
            else:
                break
        return len(s) - count
        