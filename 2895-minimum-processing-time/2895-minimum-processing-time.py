class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        tasks.sort()
        processorTime.sort(reverse=True)
        print(tasks)
        maxi = 0
        nums = []
        for i in range(3,len(tasks),4):
            nums.append(tasks[i])
        print (nums)
        for n in range(len(processorTime)):
            maxi = max(maxi,(nums[n] + processorTime[n]))
        return maxi     