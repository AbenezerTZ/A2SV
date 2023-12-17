class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        i=0
        new=[0]
        for i in range(len(gain)):
            sum=new[i]+gain[i]
            new.append(sum)
            i+=1
        return max(new)

