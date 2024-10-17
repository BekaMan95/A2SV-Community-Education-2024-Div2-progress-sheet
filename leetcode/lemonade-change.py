class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {10: 0, 5: 0}

        for num in bills:
            if num == 20:
                if change[10] and change[5]:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] > 2: change[5] -= 3
                else: return False
            elif num == 10:
                if change[5]:
                    change[10] += 1
                    change[5] -= 1
                else: return False
            else: change[5] += 1
        
        return True
