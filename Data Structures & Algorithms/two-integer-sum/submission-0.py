class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = dict()
        for i in range(len(nums)):
            if nums[i] in a:
                return [a[nums[i]], i]
            else:
                a[target - nums[i]] = i
        return [-1, -1]

        