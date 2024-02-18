class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxi = sum(accounts[0])
        for i in accounts:
            maxi = max(maxi , sum(i))
        return maxi
            