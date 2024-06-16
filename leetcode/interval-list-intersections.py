class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ptr1, ptr2, out = 0, 0, []
        while ptr1 < len(firstList) and ptr2 < len(secondList):
            low_bound = max(firstList[ptr1][0], secondList[ptr2][0])
            high_bound = min(firstList[ptr1][1], secondList[ptr2][1])
            if low_bound <= high_bound:
                out.append([low_bound, high_bound])
            if firstList[ptr1][1] > secondList[ptr2][1]:
                ptr2 += 1
            elif firstList[ptr1][1] < secondList[ptr2][1]:
                ptr1 += 1
            else:
                ptr1 += 1
                ptr2 += 1
        return out
