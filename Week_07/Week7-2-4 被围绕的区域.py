class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        if not board or len(board[0]) == 0:
            return []

        def helper(i, j):
            if board[i][j] == 'O':
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    board[x][y] = 'E'
                    offset = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for ox, oy in offset:
                        nx = x + ox
                        ny = y + oy
                        if nx < r and nx > -1 and ny < c and ny > -1:
                            if board[nx][ny] == 'O':
                                stack.append((nx, ny))

        # Traverse the edges
        r, c = len(board), len(board[0])
        for i in [0, r - 1]:
            for j in range(c):
                helper(i, j)
        for j in [0, c - 1]:
            for i in range(r):
                helper(i, j)

        for i in range(r):
            for j in range(c):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "E":
                    board[i][j] = "O"