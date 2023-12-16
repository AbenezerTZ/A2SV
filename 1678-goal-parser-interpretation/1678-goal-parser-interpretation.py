class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        i=0
        ans=""
        while i<len(command):
            if command[i]=="G":
                ans=ans + "G"
                i+=1
            elif command[i]=="(" and command[i+1]==")":
                ans=ans + "o"
                i+=2
            elif command[i]=="(" and command[i+1]=="a":
                ans=ans + "al"
                i+=4
        return ans