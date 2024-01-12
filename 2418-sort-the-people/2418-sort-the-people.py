class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        pair = []
        ans = []
        for i in range(len(names)):
            temp = []
            temp.append(heights[i])
            temp.append(names[i])
            pair.append(temp)
        pair.sort(reverse = True)
        for i in range(len(pair)):
            ans.append(pair[i][1])
        return ans
        