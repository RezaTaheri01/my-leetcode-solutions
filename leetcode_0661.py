class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        rowl, coll = len(img), len(img[0])  # Get the number of rows and columns
        smooth_img = [[0] * coll for _ in range(rowl)]  # Initialize the result image
        
        directions = [(-1, -1), (0, -1), (1, -1), (-1, 0),
                      (1, 0), (-1, 1), (0, 1), (1, 1)]  # Neighboring directions
        
        for i in range(rowl):
            for j in range(coll):
                c, sums = 0, 0
                
                # Include the current pixel itself
                for id, jd in [(0, 0)] + directions:
                    if 0 <= i + id < rowl and 0 <= j + jd < coll:
                        c += 1
                        sums += img[i + id][j + jd]

                # Calculate the average and store it in the smooth_img
                smooth_img[i][j] = sums // c  # Use integer division for rounding down
        
        return smooth_img


s = Solution()
print(s.imageSmoother(img=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(s.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]))
