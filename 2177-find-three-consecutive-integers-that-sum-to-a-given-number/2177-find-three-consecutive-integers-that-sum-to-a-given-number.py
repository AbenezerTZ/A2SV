class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        nums=[]
        if num%3==0:
            nums.append((num/3)-1)
            nums.append((num/3))
            nums.append((num/3)+1)
        return nums
            
