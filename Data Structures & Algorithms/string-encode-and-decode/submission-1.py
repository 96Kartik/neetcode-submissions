class Solution:
    def coded(self, st, encode=True):
        if encode == True:
            if len(st) == 0:
                return "$^!$"
            else:
                return "".join([chr(ord(i)-30) for i in st])
        else:
            if st == "$^!$":
                return ""
            else:
                return "".join([chr(ord(i)+30) for i in st])

    def encode(self, strs: List[str]) -> str:
        return "@*&%".join([self.coded(s, encode=True) for s in strs])
        

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        return [self.coded(i, encode=False) for i in s.split("@*&%")]
