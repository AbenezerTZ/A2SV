class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        address = address.split(".")
        new_ip = ""
        for i in address:
            new_ip = new_ip + i
            new_ip = new_ip + "[.]"
        return new_ip[:-3]