class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # If lengths differ, it's impossible to make them equal with a single swap
        if len(s) != len(goal):
            return False

        # If strings are identical, check for duplicate characters
        if s == goal:
            return len(set(s)) < len(s)

        # Collect positions where characters differ
        differences = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                differences.append((s[i], goal[i]))
                # More than two differences means no single swap can fix it
                if len(differences) > 2:
                    return False

        # Check if the two mismatched pairs can be swapped to make the strings equal
        return len(differences) == 2 and differences[0] == differences[1][::-1]


s = Solution()
print(s.buddyStrings("b", "b"))  # False
print(s.buddyStrings("bb", "bb"))  # True
print(s.buddyStrings(s="abc", goal="abc"))  # False
print(s.buddyStrings(s="abbc", goal="abbc"))  # True
print(s.buddyStrings(s="a" * 10**6 + "b", goal="a" * 10**6 + "a"))  # False
print(s.buddyStrings(s="a" * 10**6 + "bc", goal="a" * 10**6 + "cb"))  # True
print(s.buddyStrings(s="@#$", goal="$#@"))  # True
