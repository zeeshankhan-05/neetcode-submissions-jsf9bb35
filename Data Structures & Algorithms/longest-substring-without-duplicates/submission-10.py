class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupe_chars = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in dupe_chars:
                dupe_chars.remove(s[left])
                left += 1

            dupe_chars.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length