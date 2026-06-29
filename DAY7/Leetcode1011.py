class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            current_days = 1
            current_weight = 0
            
            for w in weights:
                if current_weight + w > mid:
                    current_days += 1
                    current_weight = w
                else:
                    current_weight += w
                    
            if current_days <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
