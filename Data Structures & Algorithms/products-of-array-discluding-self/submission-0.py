class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodBefore = []
        prodBefore.append(1)
        prodAfter = []
        prodAfter.append(1)
        res = []
        for i in range(len(nums) - 1):
            prodBefore.append(nums[i]*prodBefore[-1])
        for i in range(len(nums) - 1, 0, -1):
            prodAfter.append(nums[i] * prodAfter[-1])
        prodAfterReversed = []
        while prodAfter:
            prodAfterReversed.append(prodAfter.pop())
        
        for i in range(len(prodAfterReversed)):
            res.append(prodAfterReversed[i] * prodBefore[i])
        return res


        