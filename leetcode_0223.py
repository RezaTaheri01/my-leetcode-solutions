# https://www.geeksforgeeks.org/dsa/total-area-two-overlapping-rectangles/
# https://www.geeksforgeeks.org/dsa/find-two-rectangles-overlap/

class Solution: 
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def overlappingArea(l1, r1, l2, r2):
            x = 0
            y = 1
            ''' Length of intersecting part i.e  
                start from max(l1[x], l2[x]) of  
                x-coordinate and end at min(r1[x], 
                r2[x]) x-coordinate by subtracting  
                start from end we get required  
                lengths '''
            x_dist = (min(r1[x], r2[x]) -
                    max(l1[x], l2[x]))

            y_dist = (min(r1[y], r2[y]) -
                    max(l1[y], l2[y]))
            areaI = 0
            if x_dist > 0 and y_dist > 0:
                areaI = x_dist * y_dist

            return areaI

        area = abs((ax1 - ax2) * (ay1 - ay2)) + abs((bx1 - bx2) * (by1 - by2))
        
        # Find the area of overlapped section
        return area - overlappingArea((ax1, ay1), (ax2, ay2), (bx1, by1), (bx2, by2))
        
s = Solution()
print(s.computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2))
print(s.computeArea(ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2))

def do_overlap(lt1, rb1, lt2, rb2):
        # If one rectangle is to the left of the other
        if lt1[0] > rb2[0] or lt2[0] > rb1[0]:
            return False

        # If one rectangle is above the other
        if rb1[1] > lt2[1] or rb2[1] > lt1[1]:
            return False

        return True
       
