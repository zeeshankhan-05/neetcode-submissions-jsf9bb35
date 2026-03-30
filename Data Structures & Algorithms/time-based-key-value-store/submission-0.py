class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        mood, values = "", self.keys.get(key, [])
        left, right = 0, len(values) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if values[mid][1] <= timestamp:
                mood = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return mood