from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total_beams = 0
        current_row = 0

        for row in bank:
            laser_count = row.count("1")
            if laser_count != 0:
                total_beams += current_row * laser_count
                current_row = laser_count

        return total_beams


s = Solution()
print(s.numberOfBeams(bank=["011001", "000000", "010100", "001000"]))
print(s.numberOfBeams(bank=["000", "111", "000"]))

