from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []
        l = len(s)
        
        def backtracking(i, dot_counter, ip_temp):
            if dot_counter > 4:
                return
            if i == l:
                if dot_counter == 4:
                    results.append(ip_temp[:-1])
                return
              
            if s[i] == "0":
                backtracking(i + 1, dot_counter + 1, ip_temp + s[i] + ".")
            else:
                ip_part = ""
                for j in range(i, i + 3):
                    if j < l:
                        ip_part += s[j]
                        if int(ip_part) > 255:
                            break
                        backtracking(j + 1, dot_counter + 1, ip_temp + ip_part + ".")
                
        backtracking(0, 0, "")
        
        return results
            
            
        

s = Solution()

print(s.restoreIpAddresses("101023"))
print(s.restoreIpAddresses("0000"))
print(s.restoreIpAddresses("25525511135"))
print(s.restoreIpAddresses("010010"))
print(s.restoreIpAddresses("1"))
