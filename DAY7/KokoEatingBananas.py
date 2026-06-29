import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Define the binary search range
        left = 1
        right = max(piles)
        
        while left < right:
            mid_speed = left + (right - left) // 2
            
            # Calculate total hours needed at mid_speed
            total_hours = 0
            for pile in piles:
                # math.ceil(pile / mid_speed) calculates hours for each pile
                total_hours += math.ceil(pile / mid_speed)
                
            # If Koko can finish within h hours, try a slower speed
            if total_hours <= h:
                right = mid_speed
            # If it takes too long, Koko must eat faster
            else:
                left = mid_speed + 1
                
        return left
