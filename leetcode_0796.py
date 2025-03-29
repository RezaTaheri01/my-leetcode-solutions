class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        start_indexes = []
        status = False
        l = len(s)
        
        if l != len(goal):
            return False
        
        for i, char in enumerate(s):
            if char == goal[0]:
                start_indexes.append(i)
                 
        for index in start_indexes:
            status = True
            index = index - l
            for char in goal:
                if char != s[index]:
                    status = False
                    break
                index += 1
            if status:
                break
                
        return status
        
s = Solution()

print(s.rotateString(s = "abcde", goal = "cdeab"))
print(s.rotateString(s = "abcde", goal = "abced"))
        