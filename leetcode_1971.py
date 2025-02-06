from collections import deque, defaultdict

class Solution:
    def createGraph(self, n, edges):
        graph = defaultdict(set)
        for dir0, dir1 in edges:
            graph[dir0].add(dir1)
            graph[dir1].add(dir0)
        return graph

    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        if not edges:
            return False
        
        graph = self.createGraph(n, edges)
        queue = deque([source])
        visited = {source}

        while queue:
            current = queue.popleft()
            if current == destination:
                return True
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False



s = Solution()

print(s.validPath(n=3, edges=[
      [0, 1], [1, 2], [2, 0]], source=0, destination=2))
print(s.validPath(n=6, edges=[[0, 1], [0, 2], [
      3, 5], [5, 4], [4, 3]], source=0, destination=5))
