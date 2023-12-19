class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        nums =["0","1","2","3","4","5","6","7","8","9"]
        n1=n2=0
        for i in range(len(num1)): 
            product="1" + "0"*((len(num1)-1)-i)
            product = int(product)
            place = nums.index(num1[i]) * (product)
            n1+=place
            print(n1)
        for i in range(len(num2)): 
            product="1" + "0"*((len(num2)-1)-i)
            product = int(product)
            place = nums.index(num2[i]) * (product)
            n2+=place
        return str(n1 * n2)