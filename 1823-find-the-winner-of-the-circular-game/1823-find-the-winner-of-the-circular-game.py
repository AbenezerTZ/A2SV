class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        friends = list(range(1,n+1))
        pos = 0
        while len(friends) > 1:
            pos = (pos + k - 1) % len(friends)
            friends.pop(pos)
        return friends[0]