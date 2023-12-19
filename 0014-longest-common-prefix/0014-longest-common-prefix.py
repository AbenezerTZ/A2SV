class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==1:
            return strs[0]
        elif strs[0]=="" and all(s=="" for s in strs):
            return ""
        i=0
        while i<=len(strs[0]) and all(s[:i]==strs[0][:i] for s in strs):
            i+=1
        return strs[0][:i-1]


