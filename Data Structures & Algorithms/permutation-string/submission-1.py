class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1
        
        window_count = {}
        for i in range(len(s1)):
            char = s2[i]
            window_count[char] = window_count.get(char, 0) + 1

        if s1_count == window_count:
            return True

        for i in range(len(s1), len(s2)):
            new_char = s2[i]
            window_count[new_char] = window_count.get(new_char, 0) + 1

            old_char = s2[i - len(s1)]
            if window_count[old_char] == 1:
                del window_count[old_char]
            else:
                window_count[old_char] -= 1

            if s1_count == window_count:
                return True

        return False