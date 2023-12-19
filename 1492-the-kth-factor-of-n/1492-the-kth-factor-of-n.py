class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        fac=[1]
        curr=2
        while curr<=n:
            if n%curr==0:
                fac.append(curr)
                curr+=1
            else:
                curr+=1
        if k <= len(fac):
            return fac[k-1]
        else:
            return -1
