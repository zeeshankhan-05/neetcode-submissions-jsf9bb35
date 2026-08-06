class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        slowest_arrival_time = 0.0

        for car_position, car_speed in cars:
            arrival_time = (target - car_position) / car_speed

            if arrival_time > slowest_arrival_time:
                fleets += 1
                slowest_arrival_time = arrival_time

        return fleets