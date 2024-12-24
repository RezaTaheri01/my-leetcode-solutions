# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int: pass

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            guess_result: int = guess(mid)
            
            if guess_result == 0:
                return mid
            if guess_result == -1:
                r = mid - 1
            else:
                l = mid + 1 

        