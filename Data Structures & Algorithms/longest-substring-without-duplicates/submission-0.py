class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupLetters = set()
        l = 0
        longestSubstring = 0

        for r in range(len(s)):
            while s[r] in dupLetters:
                dupLetters.remove(s[l])
                l += 1
            dupLetters.add(s[r])
            longestSubstring = max(longestSubstring, r - l + 1)

        return longestSubstring