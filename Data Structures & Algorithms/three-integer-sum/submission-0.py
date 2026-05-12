class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first pass create dictionary of freq of elements
        dictA = {}
        for i in nums:
            if i not in dictA:
                dictA[i] = 0
            dictA[i] += 1
        res = set()
        res2 = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                currSum = nums[i] + nums[j]
                needed = 0 - currSum
                dictA[nums[i]] -= 1
                dictA[nums[j]] -= 1
                if needed in dictA:
                    if dictA[needed] > 0:
                        triplet = tuple(sorted(list([nums[i], nums[j], needed])))
                        res.add(triplet)
                dictA[nums[i]] += 1
                dictA[nums[j]] += 1
        for triplet in res:
            res2.append(list(triplet))
        
        return res2



            
        