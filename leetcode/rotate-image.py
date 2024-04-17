class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        dup = [[n for n in row] for row in matrix]
        for i in range(n):
            for j in range(n-1, -1, -1):
                matrix[i][n-j-1] = dup[j][i]
        """
        Do not return anything, modify matrix in-place instead.
        """
