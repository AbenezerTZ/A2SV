class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        
        x=0
        for item in operations:
            if "--" in item:
                x-=1
            if "++"in item:
                x+=1
        return x