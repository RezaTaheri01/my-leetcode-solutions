class Solution:
    def calculate(self, currentValue, target) -> int:
        counter = 0
        while target > currentValue:
            if target % 2 == 1:
                # make target even
                target += 1
                counter += 1
            target //= 2     
            counter += 1
        return counter + currentValue - target


    def brokenCalc(self, startValue: int, target: int) -> int:
        if target <= startValue:
            return startValue - target

        return self.calculate(startValue, target)


s = Solution()

print(s.brokenCalc(startValue=20, target=15))  # 5
print(s.brokenCalc(startValue=20, target=20))  # 0

print(s.brokenCalc(startValue=3, target=10))  # 3 => 10/2, 5+1, 6/2
print(s.brokenCalc(startValue=1, target=100)) # 10
print(s.brokenCalc(startValue=1, target=1000000000)) # 39
print(s.brokenCalc(startValue=68, target=100))

