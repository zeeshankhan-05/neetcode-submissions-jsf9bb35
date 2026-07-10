class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        left = 0
        length = 0

        for right in range(len(s)):
            while s[right] in letters:
                letters.remove(s[left])
                left += 1
            letters.add(s[right])
            length = max(length, right - left + 1)

        return length