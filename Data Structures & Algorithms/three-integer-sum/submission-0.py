class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i, n in enumerate(nums):
            arr = nums[:i]+nums[i+1:]
            target = 0 - n
            d = dict()
            for j, a in enumerate(arr):
                if target - a in d:
                    ans.add(",".join([str(i) for i in sorted([n, arr[d[target-a]], a])]))
                d[a] = j
        return [[int(i) for i in a.split(",")] for a in ans]
        