class Solution:
    # hash map
    def canConstructD(self, ransomNote: str, magazine: str) -> bool:
        # Create hash map of ransomNote letters
        letters = {}
        for c in ransomNote:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1

        # Search for hash map in magazine
        for c in magazine:
            if c in letters:
                if letters[c] > 1:
                    letters[c] -= 1
                else:
                    del letters[c]
                    if not letters:
                        return True

        return False

    # use python specific futures
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in set(ransomNote):
            if ransomNote.count(c) > magazine.count(c):
                return False
        return True