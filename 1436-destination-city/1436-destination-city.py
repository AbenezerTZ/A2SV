class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        start = []
        end = []
        for i in range(len(paths)):
            start.append(paths[i][0])
            end.append(paths[i][1])
        for i in end:
            if i not in start:
                return i
            
        