class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)

        if length == 1:
            return 1
        
        matrix = [[False] * length for _ in range(length)]

        for i in range(length):
            matrix[i][i] = True
        #for all possible lengths
        for j in range(2,length+1):
            for idx in range(length - j + 1):
                left = idx
                right = idx + j - 1
                if s[left] == s[right]:
                    if matrix[left + 1][right - 1] or j == 2:
                        matrix[left][right] = True

        counter = 0

        for array in matrix:
            for item in array:
                if item:
                    counter += 1
        return counter