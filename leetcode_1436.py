class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        destinations: set = {path[0] for path in paths}

        for path in paths:
            if path[1] not in destinations:
                return path[1]


s = Solution()

print(s.destCity(paths=[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
print(s.destCity(paths=[["B", "C"], ["D", "B"], ["C", "A"]]))
print(s.destCity(paths=[["A", "Z"]]))
