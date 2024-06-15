class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def rev(r: int):
            l = 0
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        ptr, out = len(arr) - 1, []
        while ptr:
            idx, max_num = 0, 0
            for i in range(ptr+1):
                if arr[i] > max_num:
                    max_num = arr[i]
                    idx = i
            if idx < ptr:
                rev(idx)
                rev(ptr)
                out.append(idx+1)
                out.append(ptr+1)
            ptr -= 1
        return out
