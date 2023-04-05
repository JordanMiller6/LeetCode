class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")
        s = Solution()
        ip_address = "1.1.1.1"
        defanged_ip_address = s.defangIPaddr(ip_address)
        print(defanged_ip_address)
