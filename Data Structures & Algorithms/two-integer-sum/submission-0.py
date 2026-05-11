class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            if nums[i] in a:
                smaller = a[nums[i]]
                return [smaller, i]
            a[target-nums[i]] = i
        


