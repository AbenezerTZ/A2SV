class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # list1 = set(list1)
        # list2 = set(list2)
        res = []
        common = set(list1).intersection(set(list2)) 
        mini = float('inf')   
        for i in common:
            if list1.index(i) + list2.index(i) < mini:
                mini = list1.index(i) + list2.index(i)
        for i in common:
            if list1.index(i) + list2.index(i) == mini:
                res.append(i)
        return res
        