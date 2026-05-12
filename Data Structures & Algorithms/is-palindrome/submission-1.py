class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        newS = ""
        stack = []
        for char in s:
            isAlpha = ord(char) <= ord('a') + 26 and ord(char) >= ord('a')
            if isAlpha or char.isdigit():
                stack.append(char)
                newS += char
        idx = 0
        while stack:
            currChar = stack.pop()
            if currChar != newS[idx]:
                return False
            idx += 1
        return True
