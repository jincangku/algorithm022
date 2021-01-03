class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        all_num = []
        for i in range(1, n + 1):
            all_num.append(i)

        output = []
        output = combinations(all_num, k)

        return output
