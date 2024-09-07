class Solution:
    challenge = []
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n
        
        left_products = 1
        for i in range(n):
            answer[i] *= left_products
            left_products *= nums[i]
            
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
         
        # O(2n) => O(n) 
        return answer
    
    
s = Solution()
print(s.productExceptSelf([1,2,3,4]))