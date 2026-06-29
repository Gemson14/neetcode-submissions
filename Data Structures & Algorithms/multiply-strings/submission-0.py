class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dictConvert = {}
        for i in range(10):
            dictConvert[f"{i}"] = i

        if num1 == "0" or num2 == "0":
            return "0"

        int1 = 0
        int2 = 0
        
        multiplier = 1
        for i in range(len(num1) - 1, -1, -1):
            intConvert = dictConvert[num1[i]]
            int1 += intConvert * multiplier
            multiplier *= 10
        
        multiplier = 1
        for i in range(len(num2) - 1, -1, -1):
            intConvert = dictConvert[num2[i]]
            int2 += intConvert * multiplier
            multiplier *= 10

        res = int1 * int2

        return str(res)






        