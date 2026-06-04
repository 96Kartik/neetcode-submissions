class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        ans = 0

        for n in nums:
            c = 0
            i = n
            while i in num_set:
                c+=1
                i+=1
            ans=max(ans,c)
        
        return ans
            


        