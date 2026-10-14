class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left=0
        right=0
        ans=0
        for right in range (0,len(nums)):
            if nums[right]==1:
                ans=max(ans,(right-left)+1)
            else:
                left=right+1
        return ans
