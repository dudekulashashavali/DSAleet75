class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        frist = float('inf')
        second = float('inf')

        for num in nums:
            if num <= frist:
                frist = num
            elif num <= second:
                second = num
            else :
                return True
        return False
        