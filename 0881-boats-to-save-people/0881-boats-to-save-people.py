class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        count = 0
        people.sort()
        i = 0
        j = len(people) - 1
        while i <= j :
            if i == j :
                return count + 1
            else:
                if people[i] + people[j] <= limit :
                    count += 1
                    i += 1
                    j -= 1
                else:
                    count += 1
                    j -= 1
        return count