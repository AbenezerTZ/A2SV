class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort()
        if len(salary)==3:
            return salary[1]
        # salary=salary[1:-1]
        result=float(sum(salary[1:-1]))/float(len(salary)-2)
        return (result)