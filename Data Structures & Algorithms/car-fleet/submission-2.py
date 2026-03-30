class Solution:
    def carFleet(self, target, position, speed):
        cars = [(position[i], (target - position[i]) / speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)

        fleets = 0
        last_time = 0

        for pos, time in cars:
            if time > last_time:
                fleets += 1
                last_time = time

        return fleets