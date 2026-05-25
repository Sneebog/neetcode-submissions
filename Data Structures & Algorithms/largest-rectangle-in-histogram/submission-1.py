class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(0,len(heights)):
            #last_index = i
            stack.append((i, heights[i]))
            while len(stack) > 1 and stack[-2][1] >= stack[-1][1]:
                print(stack)
                temp_val = stack.pop()
                val = stack.pop()
                max_area = max(max_area, (i - val[0] ) * val[1])
                #last_index = value[0]
                stack.append((val[0], temp_val[1]))
            
            #stack.append((last_index, heights[i]))
        
        while stack:
            val = stack.pop()
            print
            max_area = max(max_area, (len(heights) - val[0] ) * val[1])

        
        return max_area
