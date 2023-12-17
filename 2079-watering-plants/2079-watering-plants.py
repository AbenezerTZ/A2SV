class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        count=0
        i=0
        temp = capacity
        while i+1<len(plants):
            capacity -= plants[i]
            count+=1
            if capacity<plants[i+1]:
                count+=(i+1)*2
                capacity=temp
                i+=1
            else:
                i+=1
        if plants[-1]<=capacity:
            count+=1
        else:
            count+=((i+1)*2)+1
        return count
            
            

        