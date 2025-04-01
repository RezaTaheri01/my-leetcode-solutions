from datetime import date

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arriveAlice = [int(split) for split in arriveAlice.split("-")]
        arriveBob = [int(split) for split in arriveBob.split("-")]

        leaveAlice = [int(split) for split in leaveAlice.split("-")]
        leaveBob = [int(split) for split in leaveBob.split("-")]

        arrive = max(arriveAlice, arriveBob)
        leave = min(leaveAlice, leaveBob)

        if arrive > leave:
            return 0
        
        return (date(2018, leave[0], leave[1]) - date(2018, arrive[0], arrive[1])).days + 1
        
        


s = Solution()

print(s.countDaysTogether(arriveAlice="08-15",
      leaveAlice="08-18", arriveBob="08-16", leaveBob="08-19"))

print(s.countDaysTogether(arriveAlice="08-15",
      leaveAlice="08-18", arriveBob="08-15", leaveBob="08-19"))

print(s.countDaysTogether(arriveAlice="10-01",
      leaveAlice="10-31", arriveBob="11-01", leaveBob="12-31"))
