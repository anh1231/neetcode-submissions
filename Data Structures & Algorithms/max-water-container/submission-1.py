class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l,r = 0, len(heights) - 1
        
        while l < r:
            area = max(area, self.find_area(l,r,heights))
            if self.find_area(l + 1, r, heights) > area:
                l += 1
            elif self.find_area(l, r-1, heights) > area:
                r -= 1 
            else:
                if heights[l] <= heights[r]:
                    l+=1
                else:
                    r-=1
        return area

    def find_area(self, l, r, heights):
        return (r - l) * min(heights[l], heights[r])