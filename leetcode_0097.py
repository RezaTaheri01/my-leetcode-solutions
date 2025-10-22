from functools import lru_cache

# Problem: Time Limit Exceeded(Without Cache System)
class Solution0:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        cache = {}
        
        def recursive(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            
            result = False
            k = i + j
            if k == l3:
                result = True
            elif i < l1 and j < l2 and s1[i] == s2[j]:
                if s1[i] == s3[k]:
                    if not recursive(i+1, j):
                        result = recursive(i, j+1)
                    else:
                        result = True
                else:
                    result = False
            elif i < l1 and s1[i] == s3[k]:
                result = recursive(i+1, j)
            elif j < l2 and s2[j] == s3[k]:
                result = recursive(i, j+1)

            cache[(i, j)] = result
            return result

        if l1 + l2 != l3:
            return False

        return recursive(0, 0)

# Cleaner version + Cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False

        # Automatically memorize the outcome of function base on inputs
        @lru_cache(None)
        def recursive(i, j):
            
            k = i + j
            if k == l3:
                return True

            # try from s1
            if i < l1 and s1[i] == s3[k] and recursive(i + 1, j):
                return True

            # try from s2
            if j < l2 and s2[j] == s3[k] and recursive(i, j + 1):
                return True

            return False

        return recursive(0, 0)


s = Solution()
print(s.isInterleave("ab", "ad", "adab"))  # True
print(s.isInterleave("abcc", "dbbca", "aadbbbaccc"))  # False
print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))  # True
print(s.isInterleave("aabc", "abad", "aabadabc"))  # True
print(s.isInterleave("", "", ""))  # True
