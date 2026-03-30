class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for str in strs:
            enc += "@@@@@@@@@" + str
        return enc

    def decode(self, s: str) -> List[str]:
        return s.split("@@@@@@@@@")[1:]