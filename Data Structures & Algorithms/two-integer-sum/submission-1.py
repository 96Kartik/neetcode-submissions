class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = dict()
        for i, n in enumerate(nums):
            if target - n in r:
                return [r[target-n], i]
            r[n] = i

        