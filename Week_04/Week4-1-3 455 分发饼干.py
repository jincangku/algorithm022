class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        total = 0
        g.sort()
        s.sort()

        while (i < len(g)) and (j < len(s)):
            if g[i] <= s[j]:
                total += 1
                i += 1
                j += 1
            else:
                j += 1

        return total
