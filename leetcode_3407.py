class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        if len(p) == 1:
            return True

        # Split the pattern into prefix and suffix around the '*'
        prefix, suffix = p.split("*")
        try:
            prefix_index = s.index(prefix) + len(prefix)
        except ValueError:
            return False
        
        # Check if the suffix exists after the prefix
        return suffix in s[prefix_index:]


sol = Solution()

print(sol.hasMatch(s="leetcode", p="ee*e"))  # True
print(sol.hasMatch(s="leetcode", p="*eee"))  # False
print(sol.hasMatch(s="car", p="c*v"))  # False
print(sol.hasMatch(s="luck", p="u*"))  # True
print(sol.hasMatch(s="luck", p="*u"))  # True
print(sol.hasMatch(s="xks", p="s*"))  # True
print(sol.hasMatch(s="xlddxddlldxxdxxl", p="x*dxd"))  # True
