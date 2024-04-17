class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        max_num = max(arr)
        if arr.count(max_num) > 1:
            return False
        mono_increasing = True
        for i in range(1, len(arr)):
            if arr[i] == max_num:
                if i+1 == len(arr):
                    return False
                mono_increasing = False
            elif mono_increasing and arr[i-1] >= arr[i]:
                return False
            elif not mono_increasing and arr[i-1] <= arr[i]:
                return False
        return True
