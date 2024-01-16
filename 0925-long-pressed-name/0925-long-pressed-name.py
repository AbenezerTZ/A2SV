class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0
        j = 0
        if name[i] != typed[j]:
            return False
        while i < len(name) or j < len(typed):
            
            if i < len(name) and j < len(typed) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j >= len(typed):
                return False
            
            elif typed[j-1]==typed[j]:
                    j += 1
            else:
                return False
            
        return i == len(name) and j == len(typed)
        
        