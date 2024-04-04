class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        i = len(processorTime) - 1
        maxi = 0
        for j in range(3,len(tasks),4):
            maxi = max(maxi,(tasks[j]+processorTime[i]))
            i -= 1
        return maxi