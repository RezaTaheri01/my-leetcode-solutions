class Solution: # O(n)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash_map = {}

        for word in strs:
            # Sort the word and join to make it a string key
            sorted_word = ''.join(sorted(word)) # better than str(sorted(word))
            if sorted_word in hash_map:
                hash_map[sorted_word].append(word)
            else:
                hash_map[sorted_word] = [word]
                
        return list(hash_map.values())



s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# output => [["bat"],["nat","tan"],["ate","eat","tea"]]
