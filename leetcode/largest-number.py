class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(s1: str, s2: str):
                return -1 if int(s1+s2) > int(s2+s1) else 0

        nums = [str(n) for n in nums]
        nums = sorted(nums, key=cmp_to_key(compare))
        while len(nums) > 1 and nums[0] == '0':
            nums = nums[1:]
        return ''.join(nums)
