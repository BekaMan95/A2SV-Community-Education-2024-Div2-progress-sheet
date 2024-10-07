lass Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(pascals: list):
            nonlocal res
            if len(pascals) - 1 == rowIndex:
                res = pascals[:]
                return
            next = [1]
            for i in range(len(pascals)-1):
                next.append(pascals[i] + pascals[i+1])
            next.append(1)
            helper(next)
        
        res = []
        helper([1])
        return res
