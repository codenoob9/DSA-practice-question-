def max_area(heights):
    left = 0 
    right = len(heights) - 1 
    current_max = 0 

    while left<right :
        width = right - left 
        height = min(heights[left], heights[right] )
        current_area = width * height 

        current_max = max(current_max , current_area)

        if heights[left] < heights[right] :
            left +=1
        else:
            eight -=1

    return current_max 