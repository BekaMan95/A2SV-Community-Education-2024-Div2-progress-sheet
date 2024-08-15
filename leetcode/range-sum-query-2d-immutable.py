class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.matrix = [[0]*(cols+1) for _ in range(rows+1)]
        for r in range(rows):
            for c in range(cols):
                self.matrix[r+1][c+1] = (
                    matrix[r][c] + self.matrix[r][c+1] + self.matrix[r+1][c] - self.matrix[r][c]
                )
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.matrix[row2+1][col2+1] 
            - self.matrix[row1][col2+1] 
            - self.matrix[row2+1][col1]
            + self.matrix[row1][col1]
        )
