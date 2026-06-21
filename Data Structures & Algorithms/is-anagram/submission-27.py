class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Check if the lengths of the strings are the same
        # 2. Create 2 hashmaps to store both freq_counts
        # 3. Iterate through the strings
        # 4. For each letter, add 1 to the freq_count
        # 5. Return and compare the results of the freq_counts
        # If the same, return True. Else False

        if len(s) != len(t):
            return False
        
        freq_count_S = {}
        freq_count_T = {}

        for i in range(len(s)):
            freq_count_S[s[i]] = 1 + freq_count_S.get(s[i], 0)
            freq_count_T[t[i]] = 1 + freq_count_T.get(t[i], 0)
        
        return freq_count_S == freq_count_T