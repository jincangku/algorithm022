class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        result = ""
        for i in range(len(s) - 1, -1, -1):
            result += s[i] + " "
        return result[:-1]