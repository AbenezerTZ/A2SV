class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = []
        n = str(n)
        for i in range(len(n)):
            ans.append(int(n[i]))
        s = 0
        p = 1
        for i in ans:
            s += i
            p *= i
        return p-s