class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjMatrix = [[-1]*n for _ in range(n)]
        lowest_seen = [math.inf] * n

        for fr, to, price in flights:
            adjMatrix[fr][to] = price
        
        lowest_price = math.inf

        queue = deque()

        queue.append([src, 0, 0])

        while queue:
            currNode, currPrice, currStops = queue.popleft()
            if currStops > k:
                break
            for i in range(n): # for all nodes
                destNodePrice = adjMatrix[currNode][i]
                if destNodePrice != -1: # if there is a path
                    if i != dst: # if is not the destination
                        potential_cost = currPrice + destNodePrice
                        if potential_cost < lowest_seen[i]: #only add the node to queue if theres a shorter path to it
                            lowest_seen[i] = potential_cost
                            queue.append([i, currPrice + destNodePrice, currStops + 1])
                    else:
                        lowest_price = min(lowest_price, currPrice + destNodePrice)

        
        if lowest_price != math.inf:
            return lowest_price
        else:
            return -1




