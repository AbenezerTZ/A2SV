class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        freq = Counter(nums)
        temp = []
        for key,value in freq.items():
            temp.append(value)
        for i in temp:
            if i == 1:
                return -1
            elif i%3 == 0:
                count += i/3
            else:
                while i > 0: 
                    if i%3 == 0:
                        count += i/3
                        break
                    else:
                        count += 1
                        i -= 2
        return count