class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = {}
        for char in s1:
            s1Count[char] = s1Count.get(char, 0) + 1

        windowCount = {}
        for i in range(len(s1)):
            char = s2[i]
            windowCount[char] = windowCount.get(char, 0) + 1

        if s1Count == windowCount:
            return True

        for i in range(len(s1), len(s2)):
            newChar = s2[i]
            windowCount[newChar] = windowCount.get(newChar, 0) + 1

            oldChar = s2[i - len(s1)]
            if windowCount[oldChar] == 1:
                del windowCount[oldChar]
            else:
                windowCount[oldChar] -= 1

            if s1Count == windowCount:
                return True

        return False