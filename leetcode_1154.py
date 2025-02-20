class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        
        def is_leap_year(year: int):
            """
            Checks if a year is a leap year.

            A year is a leap year if it's divisible by 4, except for years divisible by 100 but not by 400.
            """
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return True
            else:
                return False

        days: list[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        days[1] = 29 if is_leap_year(year) else 28

        return day + sum(days[:month-1])
