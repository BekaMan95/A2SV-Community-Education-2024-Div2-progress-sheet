class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 = Counter(nums1), Counter(nums2)
        nums1, nums2 = set(nums1), set(nums2)
        out, common_values = [], nums1.intersection(nums2)
        for num in common_values:
            out += [num]*min(count1[num], count2[num])
        return out
