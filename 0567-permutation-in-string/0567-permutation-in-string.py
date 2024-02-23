class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        s1 = ''.join(sorted(s1))
        for i in range(len(s2) - window + 1):
            temp = ''.join(sorted(s2[i:i + window]))
            if temp == s1:
                return True
        return False