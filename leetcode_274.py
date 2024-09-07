class Solution:  # Chatgpt Said it's not reliable but it's like the sample code :)
    def hIndex(self, citations: list[int]) -> int:
        totalPapers = len(citations)
        citations.sort()

        for i in range(totalPapers):
            if citations[i] < totalPapers:
                totalPapers -= 1
            if citations[i] >= totalPapers:
                return totalPapers

# class Solution: # Sample code
#     def hIndex(self, citations: list[int]) -> int:
#         citations.sort()
#         n = len(citations)
#         for i in range(n):
#             if citations[i] < n:
#                 n = n - 1
#             if citations[i] >= n:
#                 return n


s = Solution()
print(s.hIndex([0]))
