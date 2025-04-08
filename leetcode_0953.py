class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_map: dict = {value: index for index, value in enumerate(order)}
        lw = len(words)

        def check_order(w1: str, w2: str):
            l1, l2 = len(w1), len(w2)
            for i in range(min(l1, l2)):
                if order_map[w1[i]] < order_map[w2[i]]:
                    return True 
                elif order_map[w1[i]] > order_map[w2[i]]:
                    return False
                
            return l1 <= l2

        for i in range(lw - 1):
            if not check_order(words[i], words[i+1]):
                return False
        return True


s = Solution()

print(s.isAlienSorted(words=["hello", "leetcode"],
      order="hlabcdefgijkmnopqrstuvwxyz"))  # True

print(s.isAlienSorted(words=["word", "world", "row"],
      order="worldabcefghijkmnpqstuvxyz"))  # False

print(s.isAlienSorted(words=["apple", "app"],
      order="abcdefghijklmnopqrstuvwxyz"))  # False

print(s.isAlienSorted(words=["apple"],
      order="abcdefghijklmnopqrstuvwxyz"))  # True
