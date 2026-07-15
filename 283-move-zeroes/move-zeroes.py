class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        c=nums.count(0)
        for i in range(c):
            nums.append(0)
            nums.remove(0)

        