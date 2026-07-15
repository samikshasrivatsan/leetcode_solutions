class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l={}
        n=len(nums)
        for i in range(n):
            x = target-nums[i]
            if x in l:
                return [l[x],i]
            l[nums[i]]=i