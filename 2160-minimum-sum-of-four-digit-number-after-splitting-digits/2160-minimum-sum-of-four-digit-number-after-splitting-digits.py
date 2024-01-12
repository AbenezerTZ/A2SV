class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = [i for i in str(num)]
        index = 0
        while index < 3:
            for i in range(index+1, 4):
                if num[index] > num[i]:
                    num[index],num[i] = num[i],num[index]
            index += 1
        return int(num[0]+num[3]) + int(num[1] + num[2])