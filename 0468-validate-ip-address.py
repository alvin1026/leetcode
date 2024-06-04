"""
https://leetcode.com/problems/validate-ip-address/description/

Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

 

Example 1:

Input: queryIP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:

Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:

Input: queryIP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.
 

Constraints:

queryIP consists only of English letters, digits and the characters '.' and ':'.
"""


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def isIP4(s):
            try:
                # check if there's any leading zeros and if the number is within the range of [0, 255]
                return str(int(s)) == s and 0 <= int(s) <= 255
            except:
                return False

        def isIP6(s):
            if len(s) > 4: return False
            if re.match(r"\W", s): return False  # if -0 is one of number
            try:
                int(s, 16)  # convert with base 16
                return True
            except:
                return False
        
        ip4 = queryIP.split(".")
        ip6 = queryIP.split(":")

        if len(ip4) == 4 and all(isIP4(n) for n in ip4):
            return "IPv4"
        if len(ip6) == 8 and all(isIP6(n) for n in ip6):
            return "IPv6"
        return "Neither"
        