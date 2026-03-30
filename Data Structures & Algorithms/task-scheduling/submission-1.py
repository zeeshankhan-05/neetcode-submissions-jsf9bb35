class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Create "groups" of the unique tasks
        # Repeat the groups as many times as available
        # Once one or more of the tasks is exhausted, insert idle/add 1 for the cooldown
        # Repeat until all tasks are completed and return the total number of cycles required (kept track by adding one for each task add in both the cooldown phases and groups)
        taskCounts = Counter(tasks)
        
        maxHeap = [-freq for freq in taskCounts.values()]
        heapq.heapify(maxHeap)

        cycles = 0
        queue = []

        while maxHeap or queue:
            cycles += 1
            if maxHeap:
                currentFreq = heapq.heappop(maxHeap)
                if currentFreq < -1:
                    queue.append((currentFreq + 1, cycles + n))

            if queue and queue[0][1] == cycles:
                heapq.heappush(maxHeap, queue.pop(0)[0])

        return cycles