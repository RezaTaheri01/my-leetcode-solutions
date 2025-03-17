class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        origins: set = {path[0] for path in paths}

        for _, dest in paths:
            if dest not in origins:
                return dest


s = Solution()

print(s.destCity(paths=[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
print(s.destCity(paths=[["B", "C"], ["D", "B"], ["C", "A"]]))
print(s.destCity(paths=[["A", "Z"]]))
