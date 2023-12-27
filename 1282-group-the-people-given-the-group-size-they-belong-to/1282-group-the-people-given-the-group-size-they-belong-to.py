class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        temp = {}
        for i, size in enumerate(groupSizes):
            if size not in temp:
                temp[size] = []
            temp[size].append(i)
        for key,value in temp.items():
            i = 0
            while i < len(value):
                ans.append(value[i:i+key])
                i += key
        return ans
