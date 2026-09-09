class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        a, b = 0, 0

        for x in nums:
            a, b = b, max(b, a + x)

        return b        