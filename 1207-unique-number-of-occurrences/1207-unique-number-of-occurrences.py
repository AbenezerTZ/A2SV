class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        result={}
        for i in arr:
            if i in result:
                result[i]+=1
            else:
                result[i]=1
        result=list(result.values())
        result=sorted(result)
        for i in range(len(result)-1):
            if result[i]==result[i+1]:
                return False
        return True
        # for i in range(len(result)):
        #     while i<len(result)-1:
        #         if result[i]==result[i+1]:    
        #             return False
        #         elif result[i]!=result[i+1]:
        #             i+=1
        #         return True