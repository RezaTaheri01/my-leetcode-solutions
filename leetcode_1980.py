class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums)
        seen = set(nums)
        
        for i in range(n+1):
            binary = bin(i)[2:].zfill(n)
            if binary not in seen:
                return binary


s = Solution()
print(s.findDifferentBinaryString(["00","01"]))
print(s.findDifferentBinaryString(["0"]))