class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        diff_heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(diff_heap, diff)
                if len(diff_heap) > ladders:
                    bricks -= heapq.heappop(diff_heap)
                if bricks < 0:
                    return i
        return len(heights) - 1