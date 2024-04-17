class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ch_total, sum_val = 0, skill[0]+skill[-1]
        left, right = 0, len(skill)-1
        while left < right:
            if skill[left]+skill[right] != sum_val:
                return -1
            ch_total += skill[left]*skill[right]
            left += 1
            right -= 1
        return ch_total
