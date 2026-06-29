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
            self.dictX[x] = set()
        self.dictX[x].add(y)

        if y not in self.dictY:
            self.dictY[y] = set()
        self.dictY[y].add(x)
        

    def count(self, point: List[int]) -> int:
        x, y = point

        # if there are matching for both x and y coordinates
        res = 0
        if x in self.dictX and y in self.dictY:
            # same x value, checking horizontal
            for y2 in self.dictX[x]:
                multiplier = self.points[(x,y2)]

                # if positive means point is above
                diff = y2 - y
            
                if diff != 0:
                    if x + diff in self.dictY[y2]:
                        multiplier = self.points[(x,y2)]
                        multiplier *= self.points[(x+diff, y2)]
                        if x + diff in self.dictY[y]:
                            multiplier *= self.points[(x+diff, y)]
                            res += multiplier


                    if x - diff in self.dictY[y2]:
                        multiplier = self.points[(x,y2)]
                        multiplier *= self.points[(x-diff, y2)]
                        if x - diff in self.dictY[y]:
                            multiplier *= self.points[(x-diff, y)]
                            res += multiplier

        return res

        

        
