class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        i = 0
        j = 1
        ans = 1
        print(nums)
        while i < len(nums) and j < len(nums):
            print("j=",nums[j], "j-1=", nums[j-1], "if=", abs(abs(nums[j]) - abs(nums[j-1])))
            if nums[j] - nums[j-1] == 1:
                j+=1
            else:
                i=j
                j+=1
            ans = max(ans, j-i)
            print("i=", i, "j=", j, "ans=", ans)
        return ans
        