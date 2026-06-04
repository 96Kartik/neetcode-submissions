class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for n in nums:
            if n in d:
                d[n]+=1
            else:
                d[n]=1
        return sorted(d,key=d.get, reverse=True)[:k]
        