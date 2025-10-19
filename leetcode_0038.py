class Solution:
    def countAndSay(self, n: int) -> str:
        current_step = "1" # We know that n is always greater than zero
        
        for _ in range(n - 1):
            counter = 1
            curr_temp = ""
            current_step += "." 
            for i in range(len(current_step) - 1):
                if current_step[i] == current_step[i + 1]:
                    counter += 1
                else:
                    curr_temp += f"{counter}{current_step[i]}"
                    counter = 1
            
            current_step = curr_temp

        return current_step


            

s = Solution()
print(s.countAndSay(8))
print(s.countAndSay(7))
print(s.countAndSay(6))
print(s.countAndSay(5))
print(s.countAndSay(4)) # 1211
print(s.countAndSay(3)) # 21
print(s.countAndSay(2)) # 11
print(s.countAndSay(1)) # 1
