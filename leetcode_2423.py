class Solution:
    def equalFrequency(self, word: str) -> bool:
        check_list = []  # prevent repeated count
        count_list = []
        for char in word:
            if char not in check_list:
                check_list.append(char)
                count_list.append(word.count(char))

        count_list_len = len(count_list)
        count_list_min = min(count_list)
        count_list_max = max(count_list)
        first_ele = count_list[0]
        first_ele_count = count_list.count(first_ele)
        count_one = count_list.count(1)

        if len(set(count_list)) > 2:
            return False
        if count_one == count_list_len:
            return True
        if count_list_len == 1 or count_list_len == 0:
            return True
        if first_ele_count == count_list_len - 1:
            if count_list_min == first_ele and first_ele + 1 == count_list_max:
                return True
            elif count_one == 1:
                return True
        if first_ele_count == 1:
            if count_list_min != first_ele and first_ele - 1 == count_list_min:
                return True
            elif first_ele == 1:
                return True

        return False


s = Solution()
print(s.equalFrequency('aaacc'))