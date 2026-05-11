class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for i in strs:
            iSorted = "".join(sorted(i))
            if iSorted in a:
                a[iSorted].append(i)
            else:
                a[iSorted] = []
                a[iSorted].append(i)
        res = []
        for key, value in a.items():
            res.append(value)
        return res
