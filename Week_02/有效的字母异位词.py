class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            count_1 = []
            count_2 = []
            for i in range(0, 26):
                count_1.append(0)
                count_2.append(0)
            for i in range(0, len(s)):
                count_1[ord(s[i]) - ord("a")] += 1
                count_2[ord(t[i]) - ord("a")] += 1
        return count_1 == count_2
