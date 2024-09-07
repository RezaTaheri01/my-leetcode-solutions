class Solution: # Slow :(
    def canJump(self, nums: list[int]) -> bool:
        i = 0
        index_list = [0]
        length = len(nums)
        num = nums[0]

        if length < 1:
            return True

        while i < length - 1:            
            if num > 0:
                i += num
                if i >= length - 1:
                    return True
                index_list.append(i)
                num = nums[i]
            else:
                while nums[i] == 0:
                    index_list.pop()
                    if not index_list:
                        return False
                    i = index_list[-1] 
                    nums[i] -= 1
                    num = nums[i]

        return True

class Solution_2:
    def canJump(self, nums: list[int]) -> int:
        maxReachable = 0
        length = len(nums)
        
        for i in range(length):
            if  i > maxReachable:
                return False
            maxReachable = max(maxReachable, i + nums[i])
            if maxReachable >= length - 1:
                return True
            
        return True

s = Solution()
print(s.canJump([2, 0, 0]))
s = Solution_2()
print(s.canJump([2, 0, 0]))
