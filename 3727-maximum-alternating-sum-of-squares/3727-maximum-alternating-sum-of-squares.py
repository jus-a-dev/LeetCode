class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = abs(nums[i])
        nums.sort()
        
        ans = 0

        low = 0
        high = n - 1

        while(low < (n / 2) ):
            ans+=(nums[high]*nums[high] - nums[low]*nums[low])
            low+=1
            high-=1

        if(n%2 != 0 ):
            ans+=(nums[int(n/2)]*nums[int(n/2)])
        return ans

        