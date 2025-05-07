class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        l, lw = len(sequence), len(word)
        start_points = dict()  # using dictionary to keep order

        # finding all word in sequence
        for i in range(l - lw + 1):
            if sequence[i: i + lw] == word:
                start_points[i] = False

        # if word not found in sequence then we return 0
        if not start_points:
            return 0

        max_c = 0
        for point in start_points.keys():
            c = -1
            if start_points[point] == False:
                while point in start_points and start_points[point] == False:
                    start_points[point] == True
                    point += lw
                    c += 1

            max_c = max(max_c, c)

        return max_c + 1



s = Solution()

print(s.maxRepeating(sequence="aaabaaaabaaabaaaabaaaabaaaabaaaaba", word="aaaba")) # 5
print(s.maxRepeating(sequence="aaaaaa", word="aa")) # 3
