class Solution:
    def rob(self, nums: List[int]) -> int:
        # at every house, i recurse to make a decision
        # 1) rob
        # 2) dont rob
        # 3) get the max
        cache = {}

        def helper(remaining):
            if remaining in cache:
                return cache[remaining]
            
            if remaining == 0:
                return 0
            if remaining == 1:
                cache[1] = nums[-1]
                return cache[1]
            if remaining == 2:
                cache[2] = max(nums[-1], nums[-2])
                return cache[2]
            else:
                firstHouseValue = nums[-1*remaining]
                cache[remaining] = max(firstHouseValue + helper(remaining-2), helper(remaining-1))
                return cache[remaining]
        
        return helper(len(nums))