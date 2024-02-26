class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        """
        :type plants: List[int]
        :type capacityA: int
        :type capacityB: int
        :rtype: int
        """
        i = 0
        j = len(plants) - 1
        a = capacityA
        b = capacityB
        count = 0
        while i <= j:
            if i == j:
                if max(a,b) < plants[i]:
                    return count + 1
                else:
                    return count
            else:
    
                if a < plants[i] and b >= plants[j]:
                    count += 1
                    a = capacityA
                elif a >= plants[i] and b < plants[j]:
                    count += 1
                    b = capacityB
                elif a < plants[i] and b < plants[j]:
                    count += 2
                    a = capacityA
                    b = capacityB                
                else:
                    a -= plants[i]
                    b -= plants[j]
                    i += 1
                    j -= 1
        return count
                