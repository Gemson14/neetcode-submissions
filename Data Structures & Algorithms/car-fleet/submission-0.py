class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_taken = []
        for i in range(len(position)):
            time_taken.append((target - position[i])/speed[i])

        sorted_list = [x for _, x in sorted(zip(position, time_taken))]

        counter = 0
        if sorted_list:
            group_limit = sorted_list.pop()
            counter += 1
        else:
            return 0

        while sorted_list:
            x = sorted_list.pop()
            if x > group_limit:
                counter += 1
                group_limit = x

        return counter
            
        