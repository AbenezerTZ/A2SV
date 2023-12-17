class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        alph=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        s=list(s)
        for i in range (1,len(s),2):
            s[i]=alph[alph.index(s[i-1])+int(s[i])]
        return ("".join(s))      
        