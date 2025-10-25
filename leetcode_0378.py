from typing import List
import numpy as np

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 1st Approach
        # pointer = [0] * len(matrix)
        
        # for _ in range(k):
        #     smallest = float("inf")
        #     point_index = None
        #     for i, p in enumerate(pointer):
        #         if p < len(matrix) and matrix[i][p] < smallest:
        #             smallest = matrix[i][p]
        #             point_index = i
        #     pointer[point_index] += 1
            
        # return matrix[point_index][pointer[point_index] - 1]
        
        # 2nd Approach (Much faster)
        arr = np.reshape(np.array(matrix), (1, len(matrix)**2))[0]
        arr.sort()
        return arr[k - 1]
        
        

s = Solution()

print(s.kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))
print(s.kthSmallest(matrix = [[-5]], k = 1))
