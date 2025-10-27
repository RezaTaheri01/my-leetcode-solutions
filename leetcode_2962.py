class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        maximum = max(nums)
        # if nums.count(maximum) < k:
        #     return 0
        
        subarrays_count = 0
        max_counter = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == maximum:
                max_counter += 1
                            
            while max_counter >= k:
                if nums[left] == maximum:
                    max_counter -= 1
                
                left += 1
            
            subarrays_count += left
                                
        return subarrays_count

s = Solution()

print(s.countSubarrays(nums=[1, 3, 2, 3, 3], k=2)) # 6
print(s.countSubarrays(nums=[1, 4, 2, 1], k=3)) # 0

print(s.countSubarrays(nums=[2, 2, 2, 2, 1, 3, 3, 2, 2, 1, 1, 3, 1,
      1, 2, 3, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 3, 1, 3, 3], k=5))  # 31

print(s.countSubarrays(nums=[61, 23, 38, 23, 56, 40, 82, 56, 82, 82,
      82, 70, 8, 69, 8, 7, 19, 14, 58, 42, 82, 10, 82, 78, 15, 82], k=2))  # 224
