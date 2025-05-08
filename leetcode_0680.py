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
        problem = False
        left, right = 0, l - 1

        while left < right:
            if s[left] != s[right]:
                if problem:
                    return False
                problem = True

                if left == 0:
                    sl = s[left + 1:]
                    sr = s[0: right]
                    resl = (sl == sl[::-1])
                    resr = (sr == sr[::-1])

                    if not (resl or resr):
                        return False
                    elif resl:
                        left += 1
                    else:
                        right -= 1
                else:
                    if not (s[right - 1] == s[left] or s[left + 1] == s[right]):
                        return False
                    # in this section we need a parallel check for each true
                    if s[left + 1] == s[right]:
                        if self.parallel_check(s, left + 1, right):
                            return True
                    if s[right - 1] == s[left]:
                        right -= 1

            left += 1
            right -= 1

        return True
    