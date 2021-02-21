class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        reverse_str = ""
        for i in range (0, len(s), 2 * k ):
           reverse_str += s[i:i+k][::-1] + s[i+k: i+2*k]
        return reverse_str