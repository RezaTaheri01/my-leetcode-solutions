from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Start with the first string as the initial prefix
        prefix = strs[0]

        for i in range(1, len(strs)):
            n = 0
            temp = strs[i]
            if len(temp) < len(prefix):
                prefix, temp = temp, prefix   
            for j in range(len(prefix)):
                if prefix[j] != temp[j]:
                    break
                n += 1
            # If the prefix becomes empty, return ""
            if n == 0:
                return ""    
            prefix = prefix[:n]   

        return prefix
    
    
s = Solution()
print(s.longestCommonPrefix(strs=["flower","flow","flight"]))