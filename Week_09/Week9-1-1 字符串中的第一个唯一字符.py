class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        h={}
        for i in s:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        for i in range(len(s)):
            if h[s[i]]==1:
                return i
        return -1