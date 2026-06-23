class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct adjacency list
        adjList = [[] for _ in range(numCourses)]

        in_degree = [0] * numCourses

        for crs, pre in prerequisites:
            adjList[pre].append(crs)
            in_degree[crs] += 1

        queue = deque()
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)

        visited = 0 
        while queue:
            visited += 1
            curr = queue.popleft()
            for i in adjList[curr]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

        return visited == numCourses
            

