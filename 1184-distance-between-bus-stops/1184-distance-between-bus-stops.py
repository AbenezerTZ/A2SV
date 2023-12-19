class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start>destination and start!=len(distance)-1:
            return min(sum(distance[0:destination]) + sum(distance[start:]),sum(distance[destination:start]))
        elif start==len(distance)-1:
            return min(sum(distance[0:destination]),sum(distance[destination+1:start]))
        else:
            return min(sum(distance[start:destination]),sum(distance[destination:]) + sum(distance[0:start]))
       