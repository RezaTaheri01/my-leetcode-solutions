class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        l = len(s)
        
        dp = [False] * (l + 1)
        dp[l] = True
        
        for i in range(l - 1, -1, -1):
            for word in wordDict:
                if len(word) + i <= l and s[i: i + len(word)] == word:
                    dp[i] = dp[i + len(word)]                    
                if dp[i]:
                    break
                
        return dp[0]
        
        # wordSet: set = set(wordDict)
        # l = len(s)

        # def recursive(start_i) -> bool:
        #     if start_i >= l:
        #         return True

        #     for w in wordDict:
        #         if s[start_i: start_i + len(w)] in wordSet:
        #             if recursive(start_i + len(w)):
        #                 return True

        #     return False

        # return recursive(0)


s = Solution()

print(s.wordBreak(s="leetcode", wordDict=["leet", "code"]))
print(s.wordBreak(s="a", wordDict=["a"]))
print(s.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
print(s.wordBreak(s="catsandog", wordDict=[
      "cats", "dog", "sand", "and", "cat"]))
print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                  ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
