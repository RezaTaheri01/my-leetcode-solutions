class Solution:
    def checkRecord(self, s: str) -> bool:
        return not ("LLL" in s or s.count("A") > 1)
