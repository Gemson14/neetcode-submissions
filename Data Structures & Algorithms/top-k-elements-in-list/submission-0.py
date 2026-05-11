class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        b = {}
        res = []
        for num in nums:
            if num not in a:
                a[num] = 1
            else:
                a[num] += 1
        for key, value in a.items():
            if value not in b:
                b[value] = []
            b[value].append(key)
        for j in range(len(nums), 0, -1):
            if j in b:
                res += b[j]
            if len(res) == k:
                break
        return res





        