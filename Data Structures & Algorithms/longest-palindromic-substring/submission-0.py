class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 1:
            return s

        matrix = [[False] * length for _ in range(length)]

        for i in range(length):
            matrix[i][i] = True

        max_length = 1
        left_idx = 0
        right_idx = 0
        
        
        #per length
        for i in range(2, length + 1):
            # all x combis of possible palindromes of length "i"
            for j in range(length - i + 1):
                left = j
                right = j + i - 1
                if s[left] == s[right]:
                    if matrix[left+1][right-1] == True or i == 2:
                        matrix[left][right] = True
                        if i > max_length:
                            max_length = i
                            left_idx = left
                            right_idx = right
        return s[left_idx:right_idx+1]

        

                
