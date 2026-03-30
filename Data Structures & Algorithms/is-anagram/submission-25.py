class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_S = {}
        freq_T = {}

        for i in range(len(s)):
            freq_S[s[i]] = 1 + freq_S.get(s[i], 0)
            freq_T[t[i]] = 1 + freq_T.get(t[i], 0)

        return freq_S == freq_T