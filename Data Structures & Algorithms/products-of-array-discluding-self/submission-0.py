class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = 1
        prefix_mul = []
        suffix_mul = []
        for i in nums:
            prefix_mul.append(a)
            a *= i
        
        b = 1
        for j in nums[::-1]:
            suffix_mul.insert(0, b)
            b *= j

        output = []
        for k in range(len(nums)):
            output.append(prefix_mul[k]*suffix_mul[k])
        
        return output



        
        