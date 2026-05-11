class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp = [nums[0]] * len(nums)
        rp = [nums[-1]]  * len(nums)
        n =len(nums)
        for i in range(1,len(nums)):
            lp[i] = lp[i-1] * nums[i]
        for i in range(n-2,-1,-1):
            rp[i] = rp[i +1] * nums[i]
    
        ans = [1] * len(nums)
        ans[0] = rp[1]
        ans[-1] = lp[-2]
        for i in range(1,n-1):
            ans[i] = lp[i - 1] * rp[i+1]
        return ans
      


        