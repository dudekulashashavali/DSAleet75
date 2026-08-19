class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ca = 0
        ha = 0
        for g in gain:
            ca += g
            ha = max(ca,ha)
        return ha
            
        

        