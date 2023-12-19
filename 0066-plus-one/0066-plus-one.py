class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        values=int(''.join(map(str,digits)))
        values=values+1
        lists=[int(ele) for ele in str(values)]
        return lists

        