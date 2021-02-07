class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])

        res, height = 0, [0] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            for j in range(n):
                if height[j] > 0:
                    l = j - 1
                    while l >= 0 and height[l] >= height[j]:
                        l -= 1

                    r = j + 1
                    while r < n and height[r] >= height[j]:
                        r += 1

                    if r - l - 1 >= height[j]:
                        res = max(res, height[j] * height[j])

        return res