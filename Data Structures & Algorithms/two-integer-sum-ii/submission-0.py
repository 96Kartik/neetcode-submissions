class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(numbers):
            if n in d:
                return [d[n], i+1]
            d[target-n] = i+1
        
        return [-1,-1]
        