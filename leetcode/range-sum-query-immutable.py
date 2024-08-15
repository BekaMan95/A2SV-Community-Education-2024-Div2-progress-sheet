class NumArray:

    def __init__(self, nums: List[int]):
        sum_val, self.nums = 0, []
        for num in nums:
            sum_val += num
            self.nums.append(sum_val)

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right] - self.nums[left-1] if left else self.nums[right]
