class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        longest_time  = 0
        longest_key = ""
        
        prev = 0
        for i, time in enumerate(releaseTimes):
            current_time = time - prev
            if current_time > longest_time:
                longest_time = current_time
                longest_key = keysPressed[i]
            elif current_time == longest_time:
                longest_key = max(longest_key, keysPressed[i])
            prev = time
        return longest_key
        
        
s = Solution()

print(s.slowestKey(releaseTimes = [9,29,49,50], keysPressed = "cbcd"))
print(s.slowestKey(releaseTimes = [12,23,36,46,62], keysPressed = "spuda"))
