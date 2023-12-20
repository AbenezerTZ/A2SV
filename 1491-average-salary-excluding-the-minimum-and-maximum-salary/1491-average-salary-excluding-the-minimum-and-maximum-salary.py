class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort()
        if len(salary)==3:
            return salary[1]
        total = sum(salary)
        return float(total - salary[0] - salary[-1]) / float(len(salary)-2)