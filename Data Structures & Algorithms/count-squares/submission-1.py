class CountSquares:

    def __init__(self):
        self.dictX = {}
        self.dictY = {}
        self.points = {}
        

    def add(self, point: List[int]) -> None:
        x, y = point
        point = tuple(point)
        if point not in self.points:
            self.points[point] = 1
        else:
            self.points[point] += 1

        if x not in self.dictX:
            self.dictX[x] = [y]
        else:
            self.dictX[x].append(y)

        if y not in self.dictY:
            self.dictY[y] = [x]
        else:
            self.dictY[y].append(x)
        

    def count(self, point: List[int]) -> int:
        x, y = point

        # if there are matching for both x and y coordinates
        res = 0
        if x in self.dictX and y in self.dictY:
            # same x value, checking horizontal
            for y2 in self.dictX[x]:

                # if positive means point is above
                diff = y2 - y
                if diff != 0:
                    for x2 in self.dictY[y2]:
                        # if same distance (left or right)
                        if abs(x2 - x) == abs(diff):
                            # if positive means point is on the right
                            diff2 = x2 - x
                            for y_test in self.dictX[x2]:
                                if y_test == y:
                                    res += 1
        

        return res

        

        
