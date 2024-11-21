class Solution:
    def parallel_check(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        l = len(s)
        problem = False  # if True => more than 1 problem found and can't be fixed
        left, right = 0, l - 1  # use two pointers

        while left < right:
            if s[left] != s[right]:
                if problem:
                    return False
                problem = True

                # try to fixing problem
                if left == 0:  # problem on edge elements 0, -1
                    sl = s[left + 1:]
                    sr = s[0: right]
                    if sl == sl[::-1]:
                        left += 1
                    elif sr == sr[::-1]:
                        right -= 1
                    else:
                        return False
                else:
                    # pass right element and compare to left => if True: continue checking
                    # pass left element and compare to right => if True: continue checking
                    if not (s[right - 1] == s[left] or s[left + 1] == s[right]):
                        return False
                    # in this section we need a parallel check for each true
                    if s[left + 1] == s[right]:
                        if self.parallel_check(s, left + 1, right):
                            return True
                    if s[right - 1] == s[left]:
                        right -= 1  # current loop check this, no need to use parallel_check

            left += 1
            right -= 1

        return True


s = Solution()
print(s.validPalindrome("ebcbbhececabbacechbbcbe"))
