class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #BFS
        adjMatrix = [[-1] * n for _ in range(n)]

        cheapestPath = [math.inf] * n
        cheapestPath[k-1] = 0

        for source, target, weight in times:
            adjMatrix[source-1][target-1] = weight
        
        queue = deque()


        for i in range(n):
            if adjMatrix[k-1][i] != -1:
                queue.append([i, adjMatrix[k-1][i]])
                cheapestPath[i] = adjMatrix[k-1][i]

        while queue:
            node, cost = queue.popleft()
            for i in range(n):
                if adjMatrix[node][i] != -1:
                    if cost + adjMatrix[node][i] < cheapestPath[i]:
                        cheapestPath[i] = cost + adjMatrix[node][i]
                        queue.append([i, cheapestPath[i]])

        if math.inf in cheapestPath:
            return -1
        return max(cheapestPath)

            

        