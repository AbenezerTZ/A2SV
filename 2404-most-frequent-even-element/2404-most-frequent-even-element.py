class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count={}
        for i in nums:
            if i in count and i%2==0:
                count[i]+=1
            elif i not in count and i%2==0:
                count[i]=1
        if not count:
            return -1 
        else: 
            large = max(count.values())
            large_key = [key for key,value in count.items() if value==large]
            return (min(large_key))
        