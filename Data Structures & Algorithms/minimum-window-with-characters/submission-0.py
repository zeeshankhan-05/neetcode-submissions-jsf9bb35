class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        have = 0
        need_count = len(need)

        left = 0
        min_len = float("inf")
        min_window = ""

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == need_count:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return min_window