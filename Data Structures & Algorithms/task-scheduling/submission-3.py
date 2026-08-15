class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26

        for task in tasks:
            count[ord(task) - ord('A')] += 1

        max_freq = max(count)
        num_max = count.count(max_freq)

        part = (max_freq - 1) * (n + 1) + num_max

        return max(len(tasks), part)