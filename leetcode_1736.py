class Solution:
    def maximumTime(self, time: str) -> str:
        h, m = time.split(":")

        # hour
        if h == "??":
            h = "23"
        else:
            if h[0] == "?":
                if int(h[1]) > 3:
                    h = "1" + h[1]
                else:
                    h = "2" + h[1]
            elif h[1] == "?":
                if int(h[0]) < 2:
                    h = h[0] + "9"
                else:
                    h = h[0] + "3"

        # minute
        if m[0] == "?":
            m = "5" + m[1]  # set first minute digit to 5
        if m[1] == "?":
            m = m[0] + "9"  # set second minute digit to 9
                   
        return h + ":" + m


s = Solution()

print(s.maximumTime(time="2?:?0"))
print(s.maximumTime(time="0?:3?"))
print(s.maximumTime(time="1?:22"))
print(s.maximumTime(time="??:??"))
