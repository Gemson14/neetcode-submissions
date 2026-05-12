class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowCheck = {}
            for j in board[i]:
                if j != "." and j in rowCheck:
                    return False
                rowCheck[j] = 1
        for i in range(9):
            colCheck = {}
            for j in range(9):
                num = board[j][i]
                if num != "." and num in colCheck:
                    return False
                colCheck[num] = 1
        for i in range(3):
            for j in range(3):
                subBoxCheck = {}
                for k in range(3):
                    for o in range(3):
                        num = board[k + 3*i][o + 3*j]
                        if num != "." and num in subBoxCheck:
                            return False
                        subBoxCheck[num] = 1
        return True

        