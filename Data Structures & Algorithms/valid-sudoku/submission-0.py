class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check all rows
        for i in range(9):
            seen = {}
            for j in range(9):
                if board[i][j] != ".":
                    seen[board[i][j]] = seen.get(board[i][j], 0) + 1
                    if seen[board[i][j]] > 1:
                        return False

        # check all columns
        for i in range(9):
            seen = {}
            for j in range(9):
                if board[j][i] != ".":
                    seen[board[j][i]] = seen.get(board[j][i], 0) + 1
                    if seen[board[j][i]] > 1:
                        return False

        for k in range(0, 9, 3):
            seen = {}
            for i in range(k, k + 3, 1):
                for j in range(3):
                    if board[i][j] != ".":
                        seen[board[i][j]] = seen.get(board[i][j], 0) + 1
                        if seen[board[i][j]] > 1:
                            return False

        for k in range(0, 9, 3):
            seen = {}
            for i in range(k, k + 3, 1):
                for j in range(3, 6):
                    if board[i][j] != ".":
                        seen[board[i][j]] = seen.get(board[i][j], 0) + 1
                        if seen[board[i][j]] > 1:
                            return False

        for k in range(0, 9, 3):
            seen = {}
            for i in range(k, k + 3, 1):
                for j in range(6, 9):
                    if board[i][j] != ".":
                        seen[board[i][j]] = seen.get(board[i][j], 0) + 1
                        if seen[board[i][j]] > 1:
                            return False

        return True