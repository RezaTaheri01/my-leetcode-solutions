class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_map: dict = {}

        for char in s:
            counter_map[char] = counter_map.get(char, 0) + 1

        for char in t:
            if char in counter_map:
                counter_map[char] -= 1
            else:
                return False

        return all(value == 0 for value in counter_map.values())
    
    

s = Solution()

print(s.isAnagram(s = "anagram", t = "nagaram")) # True
print(s.isAnagram(s = "aacc", t = "ccac")) # False
print(s.isAnagram(s = "a", t = "ab")) # False
