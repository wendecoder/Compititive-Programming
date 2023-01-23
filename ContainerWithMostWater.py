class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        fir_line= 0
        las_line = length - 1
        maxi  = 0
        while fir_line < las_line:
            high = min(height[fir_line], height[las_line])
            wide = las_line - fir_line
            newMaxi = high * wide
            maxi = max(maxi, newMaxi)
            if height[fir_line] > height[las_line]:
                las_line = las_line - 1
            else:
                fir_line = fir_line + 1
        return maxi
