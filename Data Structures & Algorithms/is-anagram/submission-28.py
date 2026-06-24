class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge case: Check if both strings are the same length
        if len(s) != len(t):
            return False

        freq_count_S = {}
        freq_count_T = {}

        for i in range(len(s)):
            freq_count_S[s[i]] = 1 + freq_count_S.get(s[i], 0)
            freq_count_T[t[i]] = 1 + freq_count_T.get(t[i], 0)

        return freq_count_S == freq_count_T