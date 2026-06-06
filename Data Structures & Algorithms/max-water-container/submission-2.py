class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        max_water = 0
        def get_trapped_water(l, r):
            if heights[l] < heights[r]:
                return (r-l)*heights[l]
            else:
                return (r-l)*heights[r]

        while i < len(heights) and j >= 0 and j>i:
            curr_water = get_trapped_water(i, j)
            print(i, j, heights[i], heights[j], curr_water, max_water)
            max_water = max(max_water, curr_water)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_water

        