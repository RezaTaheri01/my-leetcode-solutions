# Dictionaries in Python 3.7+ maintain insertion order
class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        score_to_place: dict = {key: 0 for key in score}  # ✅ Dictionary maintains original order
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        score.sort(reverse=True)  # 🚨 Sorting modifies original score list!

        for i in range(len(score)):  # Assign ranks based on sorted order
            if i < 3:
                score_to_place[score[i]] = medals[i]
            else:
                score_to_place[score[i]] = str(i + 1)

        return list(score_to_place.values())  # ✅ This follows dictionary insertion order



s = Solution()
print(s.findRelativeRanks([10, 3, 8, 9, 4]))
