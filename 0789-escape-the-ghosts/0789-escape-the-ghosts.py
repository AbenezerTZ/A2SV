class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        mini = ('inf')

        for i in range(len(ghosts)): 
            count = abs(ghosts[i][0]-target[0]) + abs(ghosts[i][1]-target[1])
            mini=min(mini,count)
        count = abs(0-target[0]) + abs(0-target[1])
        if count < mini:
            return True
        else:
            return False

