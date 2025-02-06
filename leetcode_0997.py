# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.

class Solution:
    def createGraph(self, n, trusts):
        graph = {key: set() for key in range(1, n + 1)}

        for person, trusted in trusts:
            graph[person].add(trusted)

        return graph

    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        graph = self.createGraph(n, trust)
        
        trust_nobody: list = []
        for key, value in graph.items():
            if not value:
                trust_nobody.append(key)

        if not trust_nobody:
            return -1

        # check if every person trust person in trust_nobody
        for key, value in graph.items():
            for i in range(len(trust_nobody)):
                tn = trust_nobody[i]
                if tn != 0 and key != tn and tn not in value:
                    trust_nobody[i] = 0

        return sum(trust_nobody) if sum(trust_nobody) != 0 else -1


# class Solution:
#     def findJudge(self, n: int, trust: list[list[int]]) -> int:
#         # Create an array to track trust counts for each person
#         trust_count = [0] * (n + 1)
        
#         # Process the trust relationships
#         for person, trusted in trust:
#             trust_count[person] -= 1  # person is trusting someone
#             trust_count[trusted] += 1  # trusted person is being trusted
        
#         # The town judge should have a trust count of n-1 (trusted by everyone) and trust count 0 (doesn't trust anyone)
#         for i in range(1, n + 1):
#             if trust_count[i] == n - 1:
#                 return i
        
#         return -1


s = Solution()

print(s.findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]))
print(s.findJudge(n=3, trust=[[1, 3], [2, 3]]))
print(s.findJudge(n=3, trust=[[1, 3], [2, 3]]))
print(s.findJudge(n=3, trust=[[1, 2], [2, 3]]))
print(s.findJudge(n=3, trust=[[1, 2], [2, 3], [1,3]]))
