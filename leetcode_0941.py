class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        # A valid mountain array must have at least 3 elements
        if len(arr) < 3:
            return False

        increase = False  # Flag to indicate if the array is increasing
        decrease = False  # Flag to indicate if the array is decreasing

        for i in range(len(arr) - 1):
            # if True => not strictly increasing or decreasing
            if arr[i + 1] == arr[i]:
                return False

            if arr[i + 1] > arr[i]:
                # If we've already started decreasing, return False (invalid transition)
                if decrease:
                    return False
                increase = True  # Mark that the array is increasing

            if arr[i + 1] < arr[i]:
                # If the array hasn't started increasing yet, return False
                if not increase:
                    return False
                decrease = True  # Mark that the array is decreasing

        # A valid mountain array must have both increasing and decreasing phases
        return increase and decrease


s = Solution()

print(s.validMountainArray([2, 1]))  # False
print(s.validMountainArray([3, 5, 5]))  # False
print(s.validMountainArray([0, 3, 2, 1]))  # True
print(s.validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))  # False
print(s.validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))  # False
