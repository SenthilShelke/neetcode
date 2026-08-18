class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            countSet = set()
            for j in range(9):
                if board[i][j] in countSet:
                    return False
                if board[i][j] != ".":
                    countSet.add(board[i][j])

        for j in range(9):
            countSet = set()
            for i in range(9):
                if board[i][j] in countSet:
                    return False
                if board[i][j] != ".":
                    countSet.add(board[i][j])

        for col in range(0, 9, 3):
            for row in range(0, 9, 3):
                countSet = set()
                for i in range(col, col + 3):
                    for j in range(row, row + 3):
                        if board[i][j] in countSet:
                            return False
                        if board[i][j] != ".":
                            countSet.add(board[i][j])

        return True