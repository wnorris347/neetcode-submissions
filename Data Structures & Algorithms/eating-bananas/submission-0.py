class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        floor = 1
        ceiling = max(piles)
        best_num = 0
        while floor <= ceiling:
            mid = (floor+ceiling)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours <= h:
                best_num = mid
                ceiling = mid - 1
            elif hours > h:
                floor = mid + 1
        return best_num
