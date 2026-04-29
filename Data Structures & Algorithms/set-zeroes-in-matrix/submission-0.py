import copy

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        original = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if original[i][j] == 0:
                    for a in range(len(matrix)):
                        matrix[a][j] = 0
                    for b in range(len(matrix[0])):
                        matrix[i][b] = 0

        